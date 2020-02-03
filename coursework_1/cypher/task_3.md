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
