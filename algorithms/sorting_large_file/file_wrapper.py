"""Implements a file wrapper."""


class FileWrapper:
    def __init__(self, filename):
        self._filename = filename
        self._file = open(filename)
        self._current_line = self._file.readline()

    def __lt__(self, other):
        return self._current_line < other._current_line

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
        return self._current_line is None or len(self._current_line.strip()) == 0


if __name__ == '__main__':
    f1 = FileWrapper("sorted_1.txt")
    f2 = FileWrapper("sorted_2.txt")

    l = [f1, f2]
    l.sort()

    print(l)

