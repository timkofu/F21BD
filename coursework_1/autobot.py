
# F21BD Coursework 1 Source code

import neo4j

# Bring out the cleaners
from laundry import (
    Actors,
    Movies,
    Ratings,
    RunningTimes,
    MoviesToActors
)

# Import the task executors
from bulldozer import (
    One,
    Two,
    Three
)


if __name__ == "__main__":

    try:

        # Clean data
        print("\n\n\nCleaning data ...\n")
        for cleaner in (Actors(), Movies(), Ratings(), RunningTimes(), MoviesToActors()):
            print(f"Cleaning {cleaner.__class__.__name__}")
            getattr(cleaner, 'clean')()

        # Execute tasks
        print("\n\nExecuting tasks ....\n")

    except Exception as e:
        print(f"Error: {e}")
