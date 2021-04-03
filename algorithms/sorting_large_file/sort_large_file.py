import datetime
import os
import glob

import file_wrapper
import heap as heap_lib

FileWrapper = file_wrapper.FileWrapper

LARGE_FILE_NAME = 'large.txt'
LINES_PER_FILE = 2000
SORTED_FILENAME_MASK = 'sort_data/sorted'

MinHeap = heap_lib.MinHeap


def delete_sorting_files():
    # Iterate over the list of filepaths & remove each file.
    for filePath in glob.glob(f"{SORTED_FILENAME_MASK}_*.txt"):
        try:
            print(f"Deleting: {filePath}")
            os.remove(filePath)
        except OSError:
            print("Error while deleting file")


def break_down_file(filename, lines_per_file):
    delete_sorting_files()
    lines = []
    file_index = 0
    with open(filename) as input_file:
        for line in input_file.readlines():
            lines.append(line)
            if len(lines) >= lines_per_file:
                file_index += 1
                output_file_name = f"{SORTED_FILENAME_MASK}_{file_index}.txt"
                with open(output_file_name, 'w') as output_file:
                    output_file.writelines(lines)
                lines = []
    sort_all_files()


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
    for filename in glob.glob(f"{SORTED_FILENAME_MASK}*.txt"):
        print(f"Sorting: {filename}")
        sort_file(filename)


def merge_using_qsort():
    print("Sorting using qsort")
    output_filename = f"{SORTED_FILENAME_MASK}*.txt"
    file_wrappers = [
        FileWrapper(filename)
        for filename in glob.glob(output_filename)
    ]
    started = datetime.datetime.now()
    with open(f"{SORTED_FILENAME_MASK}.txt", 'w') as output:
        counter = 0
        while file_wrappers:
            counter += 1
            if counter % 100000 == 0:
                print(counter)
            file_wrappers.sort()
            first_wrapper = file_wrappers[0]
            line = first_wrapper.current_line
            output.write(line)
            output.write('\n')
            if first_wrapper.reached_end:
                file_wrappers.remove(first_wrapper)
    finished = datetime.datetime.now()
    duration = (finished - started).total_seconds()
    print(f'duration: {duration}')
    return duration


def merge_using_heap():
    print("Sorting using heap")
    heap = MinHeap()
    for filename in glob.glob(f"{SORTED_FILENAME_MASK}_*.txt"):
        heap.add(FileWrapper(filename))

    started = datetime.datetime.now()
    with open(f"{SORTED_FILENAME_MASK}.txt", 'w') as output:
        counter = 0
        while len(heap) > 0:
            counter += 1
            if counter % 100000 == 0:
                print(counter)
            first_wrapper = heap.pop()
            line = first_wrapper.current_line
            output.write(line)
            output.write('\n')
            if not first_wrapper.reached_end:
                heap.add(first_wrapper)
    finished = datetime.datetime.now()
    duration = (finished - started).total_seconds()
    print(f'duration: {duration}')
    return duration


def check_file_sorted(filename):
    previous = None
    with open(filename) as f:
        for line in f.readlines():
            if previous and previous > line:
                return False
            previous = line
    return True


if __name__ == '__main__':
    break_down_file(LARGE_FILE_NAME, LINES_PER_FILE)

    heap_duration = merge_using_heap()
    assert check_file_sorted(f'{SORTED_FILENAME_MASK}.txt')

    qsort_duration = merge_using_qsort()
    assert check_file_sorted(f'{SORTED_FILENAME_MASK}.txt')

    print(f'heap_duration: {heap_duration}')
    print(f'qsort_duration: {qsort_duration}')
    # delete_sorting_files()
