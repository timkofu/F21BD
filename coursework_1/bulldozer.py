""" The Queries (Task 3) """

try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None  # To please PyCharm, but not needed
    print("Please install Neo4j Python library: pip install neo4j")
    exit()


class Task:
    """ Tasks base class, with shared state and behavior """

    __slots__ = (
        'n4j_handle',
    )

    def __init__(self):

        self.n4j_handle = GraphDatabase.driver(
            uri="bolt://127.0.0.1:7687",
            auth=("neo4j", input("What's your neo4j database password? ").strip()),
            encrypted=False
        )


class CreateStructure(Task):
    """
    Create the structure of the database; the nodes, labels and relationships
    """

    __slots__ = ()

    def __call__(self):

        def create_structure(tx):
            cypher = """
            CREATE 
              (`0` :Genre {director_id:'integer,',actor_id:'integer,',genre:'string'}) ,
              (`1` :Director {id:'integer,',name:'string,',rate:'float,',gross:'float,',num:'integer'}) ,
              (`2` :Movie {id:'integer,',title:'string,',year:'integer'}) ,
              (`3` :Writer {id:'integer,',name:'string'}) ,
              (`4` :Actor {id:'integer,',name:'string,',sex:'string'}) ,
              (`5` :Runningtime {country_time:'string,',addition:'string,',time:'integer'}) ,
              (`6` :Rating {rank:'float,',votes:'integer,',distribution:'integer'}) ,
              (`1`)-[:`DIRECTED` ]->(`2`),
              (`3`)-[:`WROTE` {addition:'string'}]->(`2`),
              (`4`)-[:`ACTED_IN` {as_character:'string,',leading:'integer'}]->(`2`),
              (`2`)-[:`HAS_RUNNINGTIME` ]->(`5`),
              (`2`)-[:`HAS_RATING` ]->(`6`),
              (`2`)-[:`IS_IN_GENRE` ]->(`0`),
              (`1`)-[:`DIRECTS` ]->(`0`)
            """
            for record in tx.run(cypher):
                print(record)

        with self.n4j_handle.session() as session:
            session.read_transaction(create_structure)


class ImportData(Task):
    """ Task 2B: Import data from CSVs into the database """

    def __call__(self):
        pass


class Queries(Task):
    """ Task 3: Run queries and return results """

    __slots__ = (
        'cypher_queries',
    )

    def __init__(self):

        super().__init__()

        self.cypher_queries = {
            '1': """ """,
            '2': """ """,
            '3': """ """,
            '4': """ """,
            '5': """ """,
            '6': """ """,
            '7': """ """,
            '8': """ """,
            '9': """ """,
            '10': """ """,
            '11': """ """,
            '12': """ """,
            '13': """ """,
            '14': """ """,
            '15': """ """,
        }

    def __call__(self):
        """ Execute the queries and print results """
        pass

