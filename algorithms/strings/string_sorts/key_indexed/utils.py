"""Creates testing data for the key_indexed algorithm."""

import csv
import faker
import random

_FILENAME = 'testing-data.csv'


def create_data_file(n, m):
    """Creates a file with random long sets of data to use for testing.

    :param int n: The number of strings to create.
    :param int m: The number of sections.
    :param str filename: The filename to save the data.
    """
    faker_instance = faker.Faker()
    with open(_FILENAME, 'w') as file:
        for counter, _ in enumerate(range(n)):
            name = faker_instance.name()
            sector = random.randint(1, m)
            file.write(f'"{name}",{sector}\n')
            if counter % 1000 == 0:
                print(counter)


def read_data():
    """Loads the testing data from the passed in file.

    :param str filename: The filename to load the data from.

    :returns: A list of tuples consisting of a string and a section to sort by.
    :rtype: list[Tuple[str, int]]
    """
    data = []
    with open(_FILENAME, 'r') as file:
        for tokens in csv.reader(file):
            data.append((tokens[0], int(tokens[1])))
    return data


if __name__ == '__main__':
    create_data_file(1000, 4)

