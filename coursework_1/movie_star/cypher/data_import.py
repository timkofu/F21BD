""" Importing data fro CSVs into Neo4j """

import os

from movie_star import DATA_DIRECTORY


# Generates path to datafile
def file_path_generator(file_name):
    return os.path.join(DATA_DIRECTORY, f"{file_name}.csv")


# NOTE: Can't use PERIODIC COMMIT with the driver
# Exact error: Executing queries that use periodic commit in an open transaction is not possible.
# Would have to be manual batching

DATA_IMPORT = {

    # Create constraints
    "constraints": [
        "CREATE CONSTRAINT ON (a:Actor) ASSERT a.id IS UNIQUE",
        "CREATE CONSTRAINT ON (m:Movie) ASSERT m.id IS UNIQUE",
        "CREATE CONSTRAINT ON (w:Writer) ASSERT w.id IS UNIQUE",
        "CREATE CONSTRAINT ON (d:Director) ASSERT d.id IS UNIQUE",
    ],

    # Import data
    "data_import": {

        ### Entities ###
        "entities": {

            # Actors
            "actors": """
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_actors") + """" AS row FIELDTERMINATOR ';'
                MERGE (a:Actor {id: toInteger(row.actorid), name: row.name, sex: row.sex})
                RETURN count(a)
            """,

            # Directors
            "directors": """
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("directors") + """" AS row FIELDTERMINATOR ';'
                MERGE (d:Director {id: toInteger(row.directorid), name: row.name, rate: toFloat(row.rate), gross: toFloat(row.gross), num: toInteger(row.num)})
                RETURN count(d)
            """,

            # Movies
            "movies": f"""
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_movies") + """" AS row FIELDTERMINATOR ';'
                MERGE (m:Movie {id: toInteger(row.movieid), title: row.title, year: toInteger(row.year)})
                RETURN count(m)
            """,

            # Writers
            "writers": f"""
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("writers") + """" AS row FIELDTERMINATOR ';'
                MERGE (w:Writer {id: toInteger(row.writerid), name: row.name})
                RETURN count(w)
            """,

            # Genre
            "genre": f"""
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("moviestodirectors") + """" AS row FIELDTERMINATOR ';'
                MERGE (g:Genre {movieid: toInteger(row.movieid), directorid: toInteger(row.directorid), genre: row.genre})
                RETURN count(g)
            """,

            # Rating
            "rating": f"""
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_ratings") + """" AS row FIELDTERMINATOR ';'
                MERGE (r:Rating {movieid: toInteger(row.movieid), rank: toFloat(row.rank), votes: toInteger(row.votes), distribution: row.distribution})
                RETURN count(r)
            """,

            # Running Time
            "running_time": f"""
                // USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_running_times") + """" AS row FIELDTERMINATOR ';'
                MERGE (rt:RunningTime {movieid: toInteger(row.movieid), country: row.country, addition: row.addition, time: toInteger(row.time)})
                RETURN count(rt)
            """

        },

        ### Relationships ###
        "relationships": {

            # Movie -> Rating
            "movie_rating": """
                USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_ratings") + """" AS row FIELDTERMINATOR ';'
                WITH movieid = toInteger(row.movieid)
                MATCH (m:Movie {id: movieid})
                MATCH (r:Rating {movieid: movieid})
                CREATE (m) -[:HAS_RATING]-> (r)
            """,

            # Movie -> Genre <- Director -> Movie
            "movie_director_genre": """
                USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("moviestodirectors") + """" AS row FIELDTERMINATOR ';'
                WITH directorid = toInteger(row.directorid), movieid = toInteger(row.movieid) 
                MATCH (m:Movie {id: movieid})
                MATCH (d:Director {id: directorid})
                MATCH (g:Genre {movieid: movieid, directorid: directorid})
                CREATE (d) -[:DIRECTED]-> (m)
                CREATE (d) -[:DIRECTS]-> (g)
                CREATE (m) -[:IN_GENRE]-> (g)
                
            """,

            # Movie -> RunningTime
            "movie_runningtime": """
                USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_runningtimes") + """" AS row FIELDTERMINATOR ';'
                WITH movieid = toInteger(row.movieid)
                MATCH (m:Movie {id: movieid})
                MATCH (rt:RunningTime {movieid: movieid})
                CREATE (m) -[:HAS_RUNNINGTIME]-> (rt)
            """,

            # Movie -> Writer
            "movie_writer": """
                USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("moviestowritters") + """" AS row FIELDTERMINATOR ';'
                MATCH (m:Movie {id: toInteger(row.movieid)})
                MATCH (w:Writer {id: toInteger(row.writerid)})
                CREATE (w) -[:WROTE {addition: row.addition}]-> (m)
            """,

            # Movie -> Actor
            "movie_actor": """
                USING PERIODIC COMMIT 1024
                LOAD CSV WITH HEADERS FROM "file://""" + file_path_generator("_cleaned_moviestoactors") + """" AS row FIELDTERMINATOR ';'
                MATCH (m:Movie {id: toInteger(row.movieid)})
                MATCH (a:Actor {id: toInteger(row.actorid)})
                WITH m,a
                CREATE (a) -[r:ACTED_IN {as_character: row.as_character, leading: toInteger(row.leading)}]-> (m)
            """
        }

    },

    # Create indexes based on the required queries.
    # They are slower when there already exists data in the database, but that's okay;
    # the logical progression of things is more important.
    # By default they are b-tree indexes
    "indexes": [
        "CREATE INDEX ON :Actor(sex, name, id)",
        "CREATE INDEX ON :RunningTime(time)",
        "CREATE INDEX ON :Director(name, id)",
        "CREATE INDEX ON :Movie(year, id)",
        "CREATE INDEX ON :Rating(vote)",
        "CREATE INDEX ON :Genre(genre)",
        "CREATE INDEX ON :Writer(name, id)",
    ],

}
