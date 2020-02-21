# Load data into database
Official LOAD CSV:
- Guide: https://neo4j.com/developer/guide-import-csv/
- Manual: https://neo4j.com/docs/cypher-manual/4.0/clauses/load-csv/

Sample projects:
- 


## Tips:
- Use [PERIODIC COMMIT](https://neo4j.com/docs/cypher-manual/current/query-tuning/using/#query-using-periodic-commit-hint)
- Run import commands first, then create relationships. Every import and relationship creation as a separate command.

#### Constraints
(all entered as separate commands)
- `CREATE CONSTRAINT ON (a:Actor) ASSERT a.id IS UNIQUE`
- `CREATE CONSTRAINT ON (d:Director) ASSERT d.id IS UNIQUE`
- `CREATE CONSTRAINT ON (m:Movie) ASSERT m.id IS UNIQUE`


## Entities 
#### Actors
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/actors.csv" AS row FIELDTERMINATOR ';'
    MERGE (a:Actor {id: toInteger(row.actorid), name: row.name, sex: row.sex})
    RETURN count(a)

#### Directors
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/directors.csv" AS row FIELDTERMINATOR ';'
    MERGE (d:Director {id: toInteger(row.directorid), name: row.name, rate: toFloat(row.rate), gross: toFloat(row.gross), num: toInteger(row.num)})
    RETURN count(d)

#### Movies
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/movies.csv" AS row FIELDTERMINATOR ';'
    MERGE (m:Movie {id: toInteger(row.movieid), title: row.title, year: toInteger(row.year)})
    RETURN count(m)

#### Writers
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/writers.csv" AS row FIELDTERMINATOR ';'
    MERGE (w:Writer {id: toInteger(row.writerid), name: row.name})
    RETURN count(w)

## Relationships

#### movie->rating
    // This is are movie properties, as they are attributes
    // unique to a movie
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/ratings.csv" AS row FIELDTERMINATOR ';'
    MATCH (m:Movie {id: toInteger(row.movieid)})
    SET m.rank = toFloat(row.rank)
    SET m.votes = toInteger(row.votes)
    SET m.distribution = row.distribution // Has many non-number strings and some blank cells

#### movie->director
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/moviestodirectors.csv" AS row FIELDTERMINATOR ';'
    MATCH (m:Movie {id: toInteger(row.movieid)})
    MATCH (d:Director {id: toInteger(row.directorid)})
    CREATE (m) -[:HAS_A {genre: row.genre}]-> (d)

#### movie->running_time
    // This is are movie properties, as they are attributes
    // unique to a movie
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/runningtimes.csv" AS row FIELDTERMINATOR ';'
    MATCH (m:Movie {id: toInteger(row.movieid)})
    SET m.country_time = row.time // Has mixed integer and string cells
    SET m.addition = row.addition // Many blank cells
    SET m.actual_time = toInteger(row.time1)

#### movie->writer
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/moviestowriters.csv" AS row FIELDTERMINATOR ';'
    MATCH (m:Movie {id: toInteger(row.movieid)})
    MATCH (w:Writer {id: toInteger(row.writerid)})
    CREATE (m) -[:HAS_A {addition: row.addition}]-> (w)


#### movie->actor
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///Users/timkofu/code_base/F21BD/coursework_1/data/moviestoactors.csv" AS row FIELDTERMINATOR ';'
    MATCH (m:Movie {id: toInteger(row.movieid)})
    MATCH (a:Actor {id: toInteger(row.actorid)})
    WITH m,a
    CREATE (m) -[r:HAS_AN {as_character: split(split(row.as_character,"[")[1], "]")[0], leading: toInteger(row.leading)}]-> (a)


### To-Do
- None of these cater for blank fields (they are empty strings by default)
