""" Queries to exatrct information from the database (Task 3) """

queries = {

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
        WHERE rt.actual_time < 10
        RETURN count(m)
    """,
    6: """
        MATCH (m:Movie) <-[:ACTED_IN]- (a:Actor{name: "McGregor, Ewan"})
        MATCH (m) <-[:ACTED_IN]- (:Actor{name: "Carlyle, Robert (i)"})
        RETURN m.title
    """,
    7: """
        MATCH (m:Movie) <-[:DIRECTED]- (d:Director)
        WHERE d.name STARTS WITH "Spielberg"
        RETURN count(m)
    """,
    8: """
        
    """,
    9: """ """,
    10: """ """,
    11: """
        MATCH (m:Movie)
        WHERE m.votes >= 10000
        RETURN m.title, m.votes order by m.votes desc limit 3
    """,
    12: """ """,
    13: """ """,
    14: """ """,
    15: """ """,

}
