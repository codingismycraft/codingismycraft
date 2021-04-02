import os
import glob

import file_wrapper

FileWrapper = file_wrapper.FileWrapper

def delete_sorting_files():
    # Iterate over the list of filepaths & remove each file.
    for filePath in glob.glob("sorted_*.txt", recursive=False):
        try:
            print(f"Deleting: {filePath}")
            os.remove(filePath)
        except OSError:
            print("Error while deleting file")

def break_down_file(filename, lines_per_file):
    delete_sorting_files()
    file_index = 0
    with open(filename) as input_file:
        while True:
            lines_saved_in_sorted = 0
            file_index += 1
            output_file_name = f"sorted_{file_index}.txt"
            print(f'Creating: {output_file_name}')
            line = input_file.readline()
            if not line:
                return

            with open(f"sorted_{file_index}.txt", 'w') as output_file:
                while True and lines_saved_in_sorted < lines_per_file:
                    if not line:
                        return
                    output_file.write(f'{line}')
                    lines_saved_in_sorted += 1
                    line = input_file.readline()

def sort_file(filename):
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            lines.append(line)
    lines.sort()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)


def sort_all_files():
    for filename in glob.glob("sorted_*.txt", recursive=False):
        print(f"Sorting: {filename}")
        sort_file(filename)


def merge1():
    file_wrappers = [
        FileWrapper(filename)
        for filename in glob.glob("sorted_*.txt", recursive=False)
    ]

    with open("sorted.txt", 'w') as output:
        while file_wrappers:
            file_wrappers.sort()
            first_wrapper = file_wrappers[0]
            line = first_wrapper.current_line
            output.write(line)
            output.write('\n')
            if first_wrapper.reached_end:
                file_wrappers.remove(first_wrapper)


if __name__ == '__main__':
    break_down_file('large.txt', 100)
    sort_all_files()
    merge1()
    delete_sorting_files()


