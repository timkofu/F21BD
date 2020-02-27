
try:
    from blessings import Terminal
    from colorama import init
except ImportError:
    Terminal = init = None
    print("Please install colorama and blessings: pip install colorama blessings")
    exit()

# Bring out the cleaners
from movie_star.launderer import (
    Actors,
    Movies,
    Ratings,
    RunningTimes,
    MoviesToActors
)

from movie_star.bulldozer import (
    Queries,
    ImportData,
    # CreateStructure
)
# Import the task executors


if __name__ == "__main__":

    # Initialize colorama
    init()
    # Blessings handle
    terminal = Terminal()

    try:

        # Clean data
        print("\n\n\nCleaning data ...\n")

        # No harm in running the cleaners every time the script runs, but It's nice to ask anyway
        if input("Proceed? [y/N]: ").lower() == 'y':

            for cleaner in (Actors(), Movies(), Ratings(), RunningTimes(), MoviesToActors()):
                print(f"Cleaning {cleaner.__class__.__name__}")
                cleaner()

        # No? Let's proceed to the queries then

        # Execute tasks
        print("\n\nExecuting tasks ....\n")

        # if input("This works best with a fresh neo4j database. Proceed? [Y/n]: ").lower() in ("y", ""):
        #
        #     # if input("\nCreate structure? [y/N]: ").lower() == "y":
        #     #     print("\nCreating structure ....\n")
        #     #     CreateStructure()()

        print(terminal.bold + terminal.red + "\n\n## DATA IMPORT ##\n" + terminal.normal)
        print("This works best with a fresh neo4j database")
        if input("\nImport data? [y/N]: ").lower() == "y":
            print("\nImporting data ...\n")
            ImportData()()

        print(terminal.bold + terminal.green + "\n\n## QUERIES ##\n" + terminal.normal)
        if input("Run queries? [Y/n]: ").lower() in ("y", ""):

            print("\nRunning queries ...\n")
            Queries()()

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        print(f"\nError: {e}\n")
