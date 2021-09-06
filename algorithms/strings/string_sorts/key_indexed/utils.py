"""Creates testing data for the key_indexed algorithm."""

import faker
import pickle
import random

_DEFAULT_FILENAME = 'testing-data.pickle'


def create_data_file(n, m, filename=None):
    """Creates a file with random long sets of data to use for testing.

    :param int n: The number of strings to create.
    :param int m: The number of sections.
    :param str filename: The filename to save the data.
    """
    filename = filename or _DEFAULT_FILENAME
    file = open(filename, 'wb')
    data = []
    faker_instance = faker.Faker()
    for i, _ in enumerate(range(n)):
        name = faker_instance.name()
        sector = random.randint(1, m)
        data.append((name, sector))
        if i % 1000 == 0:
            print(i)

    pickle.dump(data, file)
    file.close()


def read_data(filename=None):
    """Loads the testing data from the passed in file.

    :param str filename: The filename to load the data from.

    :returns: A list of tuples consisting of a string and a section to sort by.
    :rtype: list[Tuple[str, int]]
    """
    filename = filename or _DEFAULT_FILENAME
    file = open(filename, 'rb')
    data = pickle.load(file)
    file.close()
    return data


if __name__ == '__main__':
    create_data_file(200, 5, 'testing-data.pickle')