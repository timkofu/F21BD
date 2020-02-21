
# F21BD Coursework 1 Source code

import os

import neo4j
import pandas


# Data Cleanup
class DataCleanup:

    __slots__ = (
        'data_directory',
        'cleaned_file_prefix',
        'file_to_clean'
    )

    def __init__(self, file_to_clean):

        # All child instances need the data directory
        self.data_directory = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'data'
        )

        # And the prefix of the cleaned file
        self.cleaned_file_prefix = '_cleaned_'

        # And the file to work on
        self.file_to_clean = file_to_clean
    
    def clean(self):
        """ Template pattern method:
            - Formats the text of the file as needed
        """
        pass


class Ratings(DataCleanup):
    """ Clean the ratings file, distribution column:
        - set the empty and non-number cells to 0
    """

    __slots__ = ()
    
    def clean(self):
        
        file = os.path.join(self.data_directory, "ratings.csv")


class MoviesToWriters(DataCleanup):
    """ Clean the moviestowriters file, 'addition' column:
        - Not sure it needs cleaning ...
    """

    __slots__ = ()


class MoviesToActors(DataCleanup):
    """ Clean the moviestoactors file, 'as_character' column:
        - Remove angle brackets around character names, and <x>
          as the same number is in the 'leading' column
    """

    __slots__ = ()

    def clean(self):
        file = os.path.join(self.data_directory, "moviestoactors.csv")


class Movies(DataCleanup):
    """ Clean the movies file, 'title' column:
        - Remove quotes on title words, and any non letter and number
          characters at the beginning of titles
    """

    __slots__ = ()

    def clean(self):
        file = os.path.join(self.data_directory, "movies.csv")


class Directors(DataCleanup):
    """ Clean the directors file, 'name' column:
        - remove unicode
    """

    __slots__ = ()

    def clean(self):
        file = os.path.join(self.data_directory, "directors.csv")


class Writers(DataCleanup):
    """ Clean the writers file, 'name' column:
        - remove unicode
    """

    __slots__ = ()

    def clean(self):
        file = os.path.join(self.data_directory, "writers.csv")


class Actors(DataCleanup):
    """ Clean the directors file, 'name' column:
        - Remove quotes on title words, and any non letter and number
          characters at the beginning of names
    """

    __slots__ = ()

    def clean(self):
        file = os.path.join(self.data_directory, "actors.csv")


class RunningTimes(DataCleanup):
    """ Clean the runningtimes file, 'time' column:
        - remove numbers and leave countries only (remove appended time) as same as time1 column
        - rename time column to country, and time1 to time
    """

    __slots__ = ()

    def clean(self):
        file = os.path.join(self.data_directory, "runningtimes.csv")


# Tasks
class Task:
    """ Tasks base class, with shared state and behavior """

    __slots__ = ()

    def __init__(self):
        pass


class One(Task):

    __slots__ = ()


class Two(Task):

    __slots__ = ()


class Three(Task):

    __slots__ = ()


if __name__ == "__main__":
    pass
