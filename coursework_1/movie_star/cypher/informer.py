""" Queries to exatrct information from the database (Task 3) """

QUERIES = {

    # These are in order by question
    1: """ MATCH (a:Actor {sex: "F"}) RETURN count(a) """,
    2: """ MATCH (a:Actor {sex: "M"}) RETURN count(a) """,
    3: """
        MATCH (m:Actor {sex: "M"})
        RETURN ("Male Actors: "+count(m)) as counts
        UNION
        MATCH (f:Actor {sex: "F"})
        RETURN ("Female Actors: "+count(f)) as counts
    """,
    4: """ 
        MATCH (d:Director) -[DIRECTED]-> (m:Movie)
        WITH m, count(d) as director_count
        WHERE director_count > 6
        RETURN m.title, director_count 
    """,
    5: """
        MATCH (m:Movie) -[:HAS_RUNNINGTIME]-> (rt:RunningTime)
        WHERE rt.time < 10
        RETURN count(m)
    """,
    6: """
        MATCH (m:Movie) <-[:ACTED_IN]- (:Actor{name: "Mcgregor, Ewan"})
        MATCH (m) <-[:ACTED_IN]- (:Actor{name: "Carlyle, Robert (i)"})
        RETURN m.title
    """,
    7: """
        MATCH (m:Movie) <-[:DIRECTED]- (d:Director)
        WHERE d.name STARTS WITH "Spielberg"
        RETURN count(m)
    """,
    8: """
        MATCH (m:Actor{sex:"M"}) -[:ACTED_IN]-> (mv:Movie) <-[:ACTED_IN]- (f:Actor{sex:"F"})
        WITH count(mv) AS movie_count, f, m
        WHERE movie_count > 10
        RETURN m.name, f.name, movie_count
    """,
    9: """
        MATCH (m:Movie)
        RETURN
        CASE
        WHEN date({year: 1960}) >= m.year <= date({year: 1969})
        THEN '1960-1969'
        WHEN date({year: 1970}) >= m.year <= date({year: 1979})
        THEN '1970-1979'
        WHEN date({year: 1980}) >= m.year <= date({year: 1989})
        THEN '1980-1989'
        WHEN date({year: 1990}) >= m.year <= date({year: 1999})
        THEN '1990-1999'
        WHEN date({year: 2000}) >= m.year <= date({year: 2010})
        THEN '2000-2010'
        ELSE 'YEAR UNSPECIFIED'
        END AS result, count(*) ORDER BY result
    """,
    10: """
        MATCH (a:Actor) -[:ACTED_IN]-> (m:Movie)
        WHERE (a.sex = 'F') > (a.sex = 'M')
        WITH DISTINCT m
        RETURN count(m)
        // Wrong
    """,
    11: """
        MATCH (m:Movie)
        WHERE m.votes >= 10000
        RETURN m.title, m.votes order by m.votes desc limit 3
    """,
    12: """
        MATCH (h:Actor{name:"Hamill, Mark (i)"}), (m:Actor{name:"Mcgregor, Ewan"}),
        shortest_path = shortestPath((h) -[:ACTED_IN*1..7]- (m))
        return shortest_path
    """,
    13: """
        MATCH (a:Actor) -[:ACTED_IN]-> (m:Movie) -[:IN_GENRE]-> (g:Genre)
        WITH count(g) AS genre_count, a
        WHERE genre_count >= 10
        RETURN a.name, genre_count
    """,
    14: """
        MATCH (a:Actor) -[:ACTED_IN]-> (m:Movie) <-[:DIRECTED]- (d:Director)
        WHERE a.name = d.name
        RETURN count(m)
    """,
    15: """
        MATCH (w:Writer) -[:WROTE]-> (m:Movie) <-[:DIRECTED]- (d:Director)
        MATCH (a:Actor)
        WHERE NOT (m) <-[:ACTED_IN]- (a) AND w.name = a.name = d.name
        RETURN count(m)
    """,

}
