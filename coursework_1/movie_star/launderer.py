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

from movie_star import DATA_DIRECTORY


class DataCleanup:
    """ Base class """

    __slots__ = (
        'DATA_DIRECTORY',
        'cleaned_file_prefix',
    )

    def __init__(self):

        # And the prefix of the cleaned file
        self.cleaned_file_prefix = '_cleaned_'

    # The cleaner
    def clean(self, file_name, cleaner_function, index_column, as_str_column=None):
        """ Template pattern method:
            - Formats the text of the file as needed
        """

        # Read the file
        dataframe = pandas.read_csv(
            os.path.join(DATA_DIRECTORY, file_name),
            index_col=index_column, sep=';'
        )

        if as_str_column:
            # Change ensure it's a string, so we can use string methods on it
            dataframe[as_str_column] = dataframe[as_str_column].astype(str)

        # run custom datacleaner function
        dataframe = cleaner_function(dataframe)

        # Save the cleaned data back to csv
        dataframe.to_csv(
            os.path.join(DATA_DIRECTORY, self.cleaned_file_prefix + file_name),
            sep=";"
        )


class Ratings(DataCleanup):
    """ Clean the ratings file, distribution column:
        - set the empty and non-number cells to 0 (what does "distribution" actually mean anyway!?)
    """

    __slots__ = ()

    def __call__(self):

        file = "ratings.csv"

        # custom cleaner func
        def cfunc(dataframe):

            # Transformation:
            # - Set all non digit cells to 0
            dataframe.loc[dataframe['distribution'].apply(lambda i: not i.isdigit()), 'distribution'] = 0

            return dataframe

        # Do the actual cleaning
        self.clean(file, cfunc, index_column='movieid', as_str_column='distribution')


class MoviesToActors(DataCleanup):
    """ Clean the moviestoactors file, 'as_character' column:
        - Remove angle brackets around character names, and <x>
          as the same number is in the 'leading' column
    """

    __slots__ = ()

    def __call__(self):

        file = "moviestoactors.csv"

        # Custom cleaner func
        def cfunc(dataframe):

            def strreplace(raw_string):
                # Remove the first bracket
                cleaned_string = raw_string.replace('[', '')

                # Remove the second bracket, and everything after it in one swing
                return cleaned_string.split(']')[0]

            # Now we apply this function to every cell in column as_character
            dataframe['as_character'] = dataframe['as_character'].apply(strreplace)

            return dataframe

        self.clean(file, cfunc, index_column='movieid', as_str_column='as_character')


class Movies(DataCleanup):
    """ Clean the movies file, 'title' column:
        - Remove quotes on title words, and any non letter and number
          characters at the beginning of titles
    """

    __slots__ = ()

    def __call__(self):

        file = "movies.csv"

        def cfunc(dataframe):

            # Transformation:
            # - Remove non-alphanumeric characters

            # First compile the regex so it's fast
            regex = re.compile(r'^[^a-zA-Z\d]+')  # Remove every leading non-alphanumeric character
            dataframe['title'] = dataframe['title'].apply(lambda s: capwords(regex.sub('', s).replace("'", "")))
            # Then remove the years from the ends of titles
            regex = re.compile(r'\(\d\d\d\d\)$')
            dataframe['title'] = dataframe['title'].apply(lambda s: regex.sub('', s))

            return dataframe

        self.clean(file, cfunc, index_column='movieid', as_str_column='title')


class Actors(DataCleanup):
    """ Clean the directors file, 'name' column:
        - Remove quotes on title words, and any non letter and number
          characters at the beginning of names
    """

    __slots__ = ()

    def __call__(self):

        file = "actors.csv"

        def cfunc(dataframe):

            # Transformation:
            # - Remove non-alphanumeric characters
            # First compile the regex so it's fast
            regex = re.compile(r'^[^a-zA-Z\d]+')  # Remove every leading non-alphanumeric character
            dataframe['name'] = dataframe['name'].apply(lambda s: capwords(
                regex.sub('', s).replace("'", " ")
            ).replace("(i)", "(I)"))

            return dataframe

        self.clean(file, cfunc, index_column='actorid', as_str_column='name')


class RunningTimes(DataCleanup):
    """ Clean the runningtimes file, 'time' column:
        - remove numbers and leave countries only (remove appended time) as same as time1 column
        - rename time column to country, and time1 to time
    """

    __slots__ = ()

    def __call__(self):

        file = "runningtimes.csv"

        def cfunc(dataframe):

            # Rename time column to country
            dataframe.columns = ['country', 'addition', 'time']

            # Remove numbers and leave countries only
            dataframe.loc[dataframe['country'].apply(lambda i: i.isdigit()), 'country'] = "N"
            dataframe['country'] = dataframe['country'].apply(lambda x: x.split(":")[0])

            # Replace the NaNs with blanks
            dataframe.loc[dataframe['addition'].apply(lambda x: not type(x) == str), 'addition'] = "N"

            return dataframe

        self.clean(file, cfunc, index_column='movieid')
