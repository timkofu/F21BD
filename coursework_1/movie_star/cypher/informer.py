""" Queries to exatrct information from the database (Task 3) """

QUERIES = {

    # These are in order by question
    1: """
        // How many female actors 
        MATCH (a:Actor {sex: "F"}) RETURN count(a) 
    """,
    2: """
        // How many male actors
        MATCH (a:Actor {sex: "M"}) RETURN count(a)
    """,
    3: """
        // Find all male
        MATCH (m:Actor {sex: "M"})
        RETURN ("Male Actors: "+count(m)) as counts
        UNION
        // And female actors
        MATCH (f:Actor {sex: "F"})
        RETURN ("Female Actors: "+count(f)) as counts
        // Are there? Show me their counts
    """,
    4: """ 
        // Find movies
        MATCH (d:Director) -[DIRECTED]-> (m:Movie)
        WITH m, count(d) as director_count
        // That have more than six directors
        WHERE director_count > 6
        RETURN m.title, director_count 
    """,
    5: """
        // Find movies ...
        MATCH (m:Movie) -[:HAS_RUNNINGTIME]-> (rt:RunningTime)
        // That have a running time of less than ten minutes
        WHERE rt.time < 10
        // And tell me how many there are
        RETURN count(m)
    """,
    6: """
        // Find movies these two actors acted in
        MATCH (m:Movie) <-[:ACTED_IN]- (:Actor{name: "Mcgregor, Ewan"})
        MATCH (m) <-[:ACTED_IN]- (:Actor{name: "Carlyle, Robert (I)"})
        // And give me their titles
        RETURN m.title
    """,
    7: """
        MATCH (m:Movie) <-[:DIRECTED]- (d:Director)
        // Find movies directed by Spielberg
        WHERE d.name STARTS WITH "Spielberg"
        // And tell me how many there are
        RETURN count(m)
    """,
    8: """
        // Find male and female actors that acted in the same movie
        MATCH (m:Actor{sex:"M"}) -[:ACTED_IN]-> 
        (mv:Movie) <-[:ACTED_IN]- (f:Actor{sex:"F"})
        WITH count(mv) AS movie_count, f, m
        // If the actors have more than ten movies in common
        WHERE movie_count > 10
        // Print their names, and number of movies in common
        RETURN m.name, f.name, movie_count
    """,
    9: """
        // Get all movies
        MATCH (m:Movie)
        RETURN // Return the result of the CASE statement below
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
        // Count the movies matching each of the cases and print them ...
        END AS result, count(*) ORDER BY result
        // in ascending order.
    """,
    10: """
        // Get all movies
        MATCH (m:Movie)
        // Count the objects of each Actor type with a Movie relationship 
        WHERE size((m) <-[:ACTED_IN]- (:Actor{sex:'F'})) > size((m) <-[:ACTED_IN]- (:Actor{sex:'M'}))
        // And return the ones matching the WHERE
        RETURN count(m)
    """,
    11: """
        // Fist obtain ratings with 10000 or more votes
        MATCH (r:Rating)
        WHERE r.votes >= 10000
        // Then match said ratings to their movies
        MATCH (r) <-[:HAS_RATING]- (m:Movie)
        // Then match said movies to their Genres
        // So we can now obtain a Genre's rank via a hop
        MATCH (m) -[:IN_GENRE]-> (g:Genre)
        // Now we can obtain a Genre's rank via a hop
        // The hop is already selected above, so sum the ranks per genre
        // Collect disntict genres
        WITH collect(DISTINCT g.genre) as genres, m, r
        // Then iterate over each and collect the average rank
        // using the prior relationships
        MATCH (g:Genre) <-[:IN_GENRE]- (m) -[:HAS_RATING]-> (r)
        WHERE g.genre in genres
        return g.genre, avg(r.rank) as average_rank ORDER BY average_rank DESC LIMIT 3
    """,
    12: """
        // Find these two actors
        MATCH (h:Actor{name:"Hamill, Mark (I)"}),
        (m:Actor{name:"Mcgregor, Ewan"}),
        // And find the shortest path between them
        shortest_path = shortestPath((h) -[:ACTED_IN*]- (m))
        RETURN length(shortest_path)  // Please see screenshot in report for path diagram
    """,
    13: """
        // Find actors that acted in this movies that are in this genres
        MATCH (a:Actor) -[:ACTED_IN]-> (m:Movie) -[:IN_GENRE]-> (g:Genre)
        WITH count(g) AS genre_count, a
        // And find the actors that in genres via the movie hop
        WHERE genre_count >= 10
        // And show them to me, and how many genres they acted in
        RETURN a.name, genre_count LIMIT 10  // Please see screenshot in report for full result without the LIMIT 
    """,
    14: """
        // Find actors that acted in a movie they directed
        MATCH (a:Actor) -[:ACTED_IN]-> (m:Movie) <-[:DIRECTED]- (d:Director)
        WHERE a.name = d.name
        // And tell me how many movies have such actors
        RETURN count(m)
    """,
    15: """
        // Find writers that wrote and directed movie
        MATCH (w:Writer) -[:WROTE]-> (m:Movie) <-[:DIRECTED]- (d:Director)
        // Then get all actors
        MATCH (a:Actor)
        // Find the ones that did not also act in said movie, and were the writer and director of it
        WHERE NOT (m) <-[:ACTED_IN]- (a) AND w.name = a.name = d.name
        // And tell me how many movies there are matching this
        RETURN count(m)
    """,

}
