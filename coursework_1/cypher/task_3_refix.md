# Queries

## Questions
1. How many female actors are listed in the dataset supplied?

    - Cypher:
        - `MATCH (a:Actor {sex: "F"}) RETURN count(a)`
        
    - Answer: 32896
        
2. How many male actors are listed in the dataset supplied?

    - Cypher:
        - `MATCH (a:Actor {sex: "M"}) RETURN count(a)`
        
    - Answer: 65794 

3. Write a CYPHER query that shows the number of female actors and the number of male actors as a single query

    - Cypher:
        - `MATCH (m:Actor {sex: "M"})
        RETURN ("Male Actors: "+count(m)) as counts
        UNION
        MATCH (f:Actor {sex: "F"})
        RETURN ("Female Actors: "+count(f)) as counts`
        
    - Answer: "Male Actors: 65794" "Female Actors: 32896"

4. List the movie titles and number of directors involved for movies with more than 6 directors

    - Cypher:
        - `match(m:Movie) -[HAS_A]-> (d:Director)
        with m, count(d) as director_count
        where director_count > 6
        return m.title, director_count`
        
    - Answer: 
        - "Fantasia/2000 (1999)"	8
        - "Fantasia (1940)"	11
        - "Bambi (1942)"	7
        - "Dumbo (1941)"	7
        - "Duel in the Sun (1946)"	7
        - "Pinocchio (1940)"	7"

5. Number of movies with a running time of less than 10 minutes

    - Cypher:
        - `match (m:Movie)
        where m.actual_time < 10
        return count(m)`
        
    - Answer: 11

6. The movie titles which star both ‘Ewan McGregor’ and ‘Robert Carlyle’ (i.e. both actors were in the same film)

    - Cypher:
        - `match (m:Movie) -[:HAS_AN]-> (:Actor{name: "McGregor, Ewan"})
        match (m) -[:HAS_AN]-> (:Actor{name: "Carlyle, Robert (I)"})
        return m.title`
        
    - Answer: 
        - "Trainspotting (1996)"
        - "Being Human (1994)"
    
    - **Data cleaning needed**

7. Number of movies directed by ‘Spielberg’
    
    - Cypher:
        - `match (m:Movie) -[:HAS_A]-> (d:Director)
        where d.name starts with "Spielberg"
        return count(m)`
        
    - Answer: 14
    
    - **Data cleaning needed**

8. List the male/female actors that have worked together on more 10 films, include their names and number of films they’ve co-starred in

    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**

9. List the number of movies released per decade as listed below (1960-69, 1970-79, 1980-89,1990-99,2000-2010)

    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**

10. How many movies have more female actors than male actors?

    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**

11. Based ratings with 10,000 or more votes, what are the top 3 movie genres using the average rank per movie genre as the metric? (Note: where a higher value for rank is considered a better movie)

    - Cypher:
        - `match (m:Movie)
        where m.votes >= 10000
        return m.title, m.votes order by m.votes desc limit 3`
        
    - Answer:
        - "The Shawshank Redemption (1994)"	998823
        "Pulp Fiction (1994)"	775943
        "Fight Club (1999)"	759494

12. Show the shortest path between actors ‘Ewan McGregor’ and ‘Mark Hamill’ from the IMDB data subset. Include nodes and edges – answer can be shown as an image or text description in form (a)-[ ]->(b)-[ ]-> (c)…

    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**

13. List all actors (male/female) that have starred in 10 or more different film genres (show names, and number of genres)

    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**

14. How many movies have an actor/actress that also directed the movie?

    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**

15. How many movies have been written and directed by an actor/actress that they didn’t star in? (i.e. the person who wrote and directed the movie is a film star but didn’t appear in the movie)
    
    - Cypher:
        - ``
     
    - Answer:
    
    - **Better modeling needed**