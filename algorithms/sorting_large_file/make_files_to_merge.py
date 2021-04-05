"""Utility to create a large amount of files to sort.

The files created from this utility simulate the breakdown of a huge
file to smaller sorted files exactly as it happens in the related
algorithm.

Doing so allows us to concentrate on the file merging algorithm and
relieves us from the details that have to do with the breaking of the
huge file to smaller sorted files.  Also it allows us to creating our
testing data in a self-sufficient manner without having to rely on
an external source where to download the "huge" file from.
"""

import faker
import os

SORTED_FILE_NAME_MASK = "./sorted_files/sorted_{index}".format
NUMBER_OF_LINES_PER_FILE = 1000
MAX_LINE_LENGTH = 70
NUMBER_OF_FILES_TO_CREATE = 200

fake_gen = faker.Faker()


def make_file(file_index, count):
    """Makes a file containing random data.

    :param int file_index: The "index" of the file to create.
    :param int count: The number of rows to add to the file.

    :returns: The number of lines in the file that was created.
    :rtype: int
    """
    filename = SORTED_FILE_NAME_MASK(index=file_index)
    print(f"Creating: {filename}")
    lines = [
        fake_gen.text(MAX_LINE_LENGTH).lower().replace(' ', '')
        for _ in range(count)
    ]
    lines.sort()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(f'{line}\n')
    return len(lines)


def make_all(count):
    """Makes the 'smaller' sorted files.

    :param int count: The number of "smaller and sorted" files to create.
    """
    os.system("mkdir -p ./sorted_files")
    os.system("mkdir -p ./solution")
    os.system("rm ./sorted_files/*")
    os.system("rm ./solution/*")
    total_lines = 0
    total_files_created = 0
    for index in range(1, count + 1):
        total_lines += make_file(index, NUMBER_OF_LINES_PER_FILE)
        total_files_created += 1
    print(f"File created: {total_files_created}\n"
          f"Total number of lines: {total_lines}")


if __name__ == '__main__':
    print(f"Creating {NUMBER_OF_FILES_TO_CREATE} sorted files.")
    make_all(NUMBER_OF_FILES_TO_CREATE)
