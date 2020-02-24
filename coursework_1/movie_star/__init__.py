""" F21BD 2019-2020 Coursework One """

import os


# Location of CSV files, shared across the module
DATA_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data'
)

# Check the existance of the data before we even do anything else
if not os.path.isdir(DATA_DIRECTORY):
    print(
        f"Data directory doesn't exist.{os.linesep}"
        "Please create a directory called 'data' in the same place as me, "
        "downloaded data files from here http://www.macs.hw.ac.uk/~pb56/f21bd.html) "
        "and extract them inside it."
    )
    exit()

# We have the directory, but do we have the data files?
expected_data_files = [
    'directors.csv',
    'moviestoactors.csv',
    'moviestowriters.csv',
    'runningtimes.csv',
    'actors.csv',
    'movies.csv',
    'moviestodirectors.csv',
    'ratings.csv',
    'writers.csv'
]

for d in expected_data_files:
    if not os.path.isfile(os.path.join(DATA_DIRECTORY, d)):
        print(f"{d} is missing.")
        exit()
