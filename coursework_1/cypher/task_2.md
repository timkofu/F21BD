# Load data into database
Official LOAD CSV:
- Guide: https://neo4j.com/developer/guide-import-csv/
- Manual: https://neo4j.com/docs/cypher-manual/4.0/clauses/load-csv/


## Tips:
- Use [PERIODIC COMMIT](https://neo4j.com/docs/cypher-manual/current/query-tuning/using/#query-using-periodic-commit-hint)
- Run import commands first, then create relationships. Every import and relationship creation as a separate command.
## Entities 
#### Actors
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///...actors.csv"

#### Directors
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///...directors.csv"

#### Movies
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///...movies.csv"

#### Writers
    USING PERIODIC COMMIT 1024
    LOAD CSV WITH HEADERS FROM "file:///...writers.csv"

## Relationships

#### movie->rating

#### movie->director

#### movie->running_time

#### movie->writer

#### movie->actor
