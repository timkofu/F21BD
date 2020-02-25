""" The Queries (Task 3) """

from getpass import getpass

try:
    from neo4j import GraphDatabase
except ImportError:
    GraphDatabase = None  # To please PyCharm, but not needed
    print("Please install Neo4j Python library: pip install neo4j")
    exit()

from movie_star import DATA_DIRECTORY
from movie_star.cypher.structure import CREATE_STRUCTURE
from movie_star.cypher.data_import import DATA_IMPORT


class Task:
    """ Tasks base class, with shared state and behavior """

    __slots__ = (

    )

    # Neo4J database handle
    # (static variable, so only needs to be created once an all child
    # classes have access to it)

    try:

        n4j_handle = GraphDatabase.driver(
            uri="bolt://127.0.0.1:7687",
            auth=("neo4j", getpass("\nWhat's your neo4j database password? ").strip()),
            encrypted=False
        )

    except Exception as e:

        print("Sorry, we could not connect to your Neo4j database.")
        error = str(e)
        if len(error) > 2:
            print(f"Error: {error}")
        exit()

    # Cypher runner
    def run_cypher(self, cypher_command):
        """
        Runs a given cypher query/command
        (Could be better; will improve in the optimization iteration)

        :param cypher_command:
        :return: None
        """
        def runner(tx):
            for record in tx.run(cypher_command):
                print(record)

        with self.n4j_handle.session() as session:
            session.read_transaction(runner)


# class CreateStructure(Task):
#     """
#     Create the structure of the database; the nodes, labels and relationships
#     """
#
#     __slots__ = ()
#
#     def __call__(self):
#
#         self.run_cypher(CREATE_STRUCTURE)


class ImportData(Task):
    """ Task 2B: Import data from CSVs into the database """

    def __constraints(self):
        """ Create constraints"""
        for constraint in DATA_IMPORT['constraints']:
            self.run_cypher(constraint)

    def __entities(self):
        """ Import and create entities"""
        entity_creation_commands = DATA_IMPORT['data_import']['entities']
        for entity in entity_creation_commands.keys():
            self.run_cypher(entity_creation_commands[entity])

    def __relationships(self):
        """ Import and create relationships"""
        relationships = DATA_IMPORT['data_import']['relationships']
        for rel in relationships.keys():
            self.run_cypher(relationships[rel])

    def __indexes(self):
        """ Create indexes """
        for index in DATA_IMPORT['indexes']:
            self.run_cypher(index)

    def __call__(self):

        if input("Create constraints? [y/N]: ").lower() == "y":
            print("\nCreating constraints ...\n")
            self.__constraints()

        if input("Create entities? [y/N]: ").lower() == "y":
            print("\nCreating entities ...\n")
            self.__entities()

        if input("Create relationships? [y/N]: ").lower() == "y":
            print("\nCreating relationships ...\n")
            self.__relationships()

        if input("Create indexes? [y/N]: ").lower() == "y":
            print("\nCreating indexes ...\n")
            self.__indexes()


class Queries(Task):
    """ Task 3: Run queries and return results """

    def __call__(self):
        """ Execute the queries and print results """
        pass

