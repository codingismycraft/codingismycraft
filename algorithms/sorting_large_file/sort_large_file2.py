"""Merges an array of sorted files to single sorted file."""

import datetime
import glob

import heapq


SORTED_FILENAME_MASK = './sorted_files/sorted'
OUTPUT_FILE = './solution/sorted.txt'
OUTPUT_FILE_FROM_MERGE = './solution/sorted_with_buildin_heap.txt'


HEAP = []

class FileWrapper:
    def __init__(self, filename):
        self._filename = filename
        self._file = open(filename)
        self._current_line = self._file.readline()

    def __lt__(self, other):
        return self._current_line < other._current_line

    def __le__(self, other):
        return self._current_line <= other._current_line

    def __repr__(self):
        return self._filename

    @property
    def current_line(self):
        if self.reached_end:
            return None
        line = self._current_line
        line = line.strip()
        self._current_line = self._file.readline()
        return line

    @property
    def reached_end(self):
        return self._current_line is None or len(
            self._current_line.strip()) == 0


def check_sorted_subfiles():
    mask = f"{SORTED_FILENAME_MASK}_*"

    for filename in glob.glob(mask):
        print(f'checking {filename}')
        assert check_file_sorted(filename)


def merge_using_heap():
    print("Sorting using heap")

    mask = f"{SORTED_FILENAME_MASK}_*"
    for filename in glob.glob(mask):
        heapq.heappush(HEAP, FileWrapper(filename))
    started = datetime.datetime.now()
    with open(OUTPUT_FILE_FROM_MERGE, 'w') as output:
        counter = 0
        while len(HEAP) > 0:
            counter += 1
            if counter % 100000 == 0:
                print(counter)
            first_wrapper = heapq.heappop(HEAP)
            line = first_wrapper.current_line
            output.write(line)
            output.write('\n')
            if not first_wrapper.reached_end:
                heapq.heappush(HEAP, first_wrapper)
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
    merge_using_heap()
    assert check_file_sorted(OUTPUT_FILE_FROM_MERGE)
