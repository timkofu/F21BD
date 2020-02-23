""" Data cleaning (Task 2A) """

import os
import re
from string import capwords

try:
    import pandas
except ImportError:
    pandas = None  # To please PyCharm, but not needed
    print("Please install Pandas: pip install pandas")
    exit()


class DataCleanup:
    """ Base class """

    __slots__ = (
        'data_directory',
        'cleaned_file_prefix',
    )

    def __init__(self):

        # All child instances need the data directory
        self.data_directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'data'
        )

        # And the prefix of the cleaned file
        self.cleaned_file_prefix = '_cleaned_'

        # Check existance of data files
        if not os.path.isdir(self.data_directory):
            print(
                f"Data directory doesn't exist.{os.linesep}"
                f"Please create a directory called data and put the data files inside it."
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
            if not os.path.isfile(os.path.join(self.data_directory, d)):
                print(f"{d} is missing.")
                exit()

    def clean(self):
        """ Template pattern method:
            - Formats the text of the file as needed
        """

        # CSV file name
        file = None


class Ratings(DataCleanup):
    """ Clean the ratings file, distribution column:
        - set the empty and non-number cells to 0 (what does "distribution" actually mean anyway!?)
    """

    __slots__ = ()

    def clean(self):
        file = "ratings.csv"

        # Read the file
        dataframe = pandas.read_csv(
            os.path.join(self.data_directory, file),
            index_col='movieid', sep=';', dtype={'distribution': object}
        )

        # Change it to a string, so we can use the isdigit string method to find non-digits
        dataframe['distribution'] = dataframe['distribution'].astype(str)

        # Transformation:
        # - Set all non digit cells to 0
        dataframe.loc[dataframe['distribution'].apply(lambda i: not i.isdigit()), 'distribution'] = 0

        # Save the cleaned data back to csv
        dataframe.to_csv(
            os.path.join(self.data_directory, self.cleaned_file_prefix + file)
        )


class MoviesToActors(DataCleanup):
    """ Clean the moviestoactors file, 'as_character' column:
        - Remove angle brackets around character names, and <x>
          as the same number is in the 'leading' column
    """

    __slots__ = ()

    def clean(self):

        file = "moviestoactors.csv"

        # Read the file
        dataframe = pandas.read_csv(
            os.path.join(self.data_directory, file),
            index_col='movieid', sep=';'
        )

        # Make sure the as_character column is of datatype string
        dataframe['as_character'] = dataframe['as_character'].astype(str)

        # Transformation:
        # - Remove angle brackets around character names, and <x>

        def clean_string(string):
            """ Does the transformation """

            # Remove the first bracket
            cleaned_string = string.replace('[', '')

            # Remove the second bracket, and everything after it in one swing
            cleaned_string = cleaned_string.split(']')[0]

            # Return cleaned string
            return cleaned_string

        # Now we apply this function to every cell in column as_character
        dataframe['as_character'] = dataframe['as_character'].apply(clean_string)

        # And save the cleaned data as csv
        dataframe.to_csv(
            os.path.join(self.data_directory, self.cleaned_file_prefix + file)
        )


class Movies(DataCleanup):
    """ Clean the movies file, 'title' column:
        - Remove quotes on title words, and any non letter and number
          characters at the beginning of titles
    """

    __slots__ = ()

    def clean(self):
        file = "movies.csv"

        # Read the file
        dataframe = pandas.read_csv(
            os.path.join(self.data_directory, file),
            index_col='movieid', sep=';'
        )

        # Make sure the title column is of datatype string
        dataframe['title'] = dataframe['title'].astype(str)

        # Transformation:
        # - Remove non-alphanumeric characters
        # First compile the regex so it's fast
        regex = re.compile(r'^[^a-zA-Z\d]+')  # Remove every leading non-alphanumeric character
        dataframe['title'] = dataframe['title'].apply(lambda s: capwords(regex.sub('', s).replace("'", "")))

        # And save the cleaned data as csv
        dataframe.to_csv(
            os.path.join(self.data_directory, self.cleaned_file_prefix + file)
        )


class Actors(DataCleanup):
    """ Clean the directors file, 'name' column:
        - Remove quotes on title words, and any non letter and number
          characters at the beginning of names
    """

    __slots__ = ()

    def clean(self):
        file = "actors.csv"

        # Read the file
        dataframe = pandas.read_csv(
            os.path.join(self.data_directory, file),
            index_col='actorid', sep=';'
        )

        # Make sure the title column is of datatype string
        dataframe['name'] = dataframe['name'].astype(str)

        # Transformation:
        # - Remove non-alphanumeric characters
        # First compile the regex so it's fast
        regex = re.compile(r'^[^a-zA-Z\d]+')  # Remove every leading non-alphanumeric character
        dataframe['name'] = dataframe['name'].apply(lambda s: capwords(regex.sub('', s).replace("'", " ")))

        # And save the cleaned data as csv
        dataframe.to_csv(
            os.path.join(self.data_directory, self.cleaned_file_prefix + file)
        )


class RunningTimes(DataCleanup):
    """ Clean the runningtimes file, 'time' column:
        - remove numbers and leave countries only (remove appended time) as same as time1 column
        - rename time column to country, and time1 to time
    """

    __slots__ = ()

    def clean(self):
        file = "runningtimes.csv"

        # The usual ..
        dataframe = pandas.read_csv(
            os.path.join(self.data_directory, file),
            index_col='movieid', sep=';'
        )

        # Rename time column to country
        dataframe.columns = ['country', 'addition', 'time']

        # Remove numbers and leave countries only
        dataframe.loc[dataframe['country'].apply(lambda i: i.isdigit()), 'country'] = ""
        dataframe['country'] = dataframe['country'].apply(lambda x: x.split(":")[0])

        # Replace the NaNs with blanks
        dataframe.loc[dataframe['addition'].apply(lambda x: not type(x) == str), 'addition'] = ""

        # And save the cleaned data as csv
        dataframe.to_csv(
            os.path.join(self.data_directory, self.cleaned_file_prefix + file)
        )
