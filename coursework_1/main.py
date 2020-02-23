
# F21BD Coursework 1 Source code

# Bring out the cleaners
from launderer import (
    Actors,
    Movies,
    Ratings,
    RunningTimes,
    MoviesToActors
)

from bulldozer import (
    Queries,
    ImportData,
    CreateStructure
)
# Import the task executors


if __name__ == "__main__":

    try:

        # Clean data
        print("\n\n\nCleaning data ...\n")

        # No harm in running the cleaners every time the script runs, but It's nice to ask anyway
        if input("Do I proceed? [y/n]: ").lower() == 'y':

            for cleaner in (Actors(), Movies(), Ratings(), RunningTimes(), MoviesToActors()):
                print(f"Cleaning {cleaner.__class__.__name__}")
                cleaner()

        # No? Let's proceed to the queries then

        # Execute tasks
        print("\n\nExecuting tasks ....\n")

        if input("This needs a fresh neo4j database. Proceed? [y/n]: ").lower() == 'y':

            # Let's first create the structure
            print("\nCreating structure ....\n")
            CreateStructure()()

            print("\nImporting data ...\n")
            ImportData()()

            print("\nRunning queries ...\n")
            Queries()()

    except KeyboardInterrupt:
        exit()
    except Exception as e:
        raise
        print(f"Error: {e}")
