"""Solves the Student Attendance Record Problem."""

class RecordStatus:
    """Solves the Student Attendance Record Problem.

    :ivar int _has_a_ends_with_p: The counter of records that contain an
    "Absent" and end with Present.

    :ivar int _ends_with_p: The counter of records that contain an
    ending with Present (not containing absent).

    :ivar int _has_a_ends_with_l: The counter of records that contain an
    "Absent" and end with Late.

    :ivar int _ends_with_l: The counter of records that contain an
    ending with a single Late (not containing absent).

    :ivar int _has_a_ends_with_ll: The counter of records that contain an
    "Absent" and end with double Late.

    :ivar int _ends_with_ll: The counter of records that contain an
    ending with a double Late (LL)(not containing absent).

    :ivar int _ends_with_a: The counter of records ending with Absent (A).
    """

    def __init__(self):
        """Initializes the record."""
        self._has_a_ends_with_p = 0
        self._ends_with_p = 1
        self._has_a_ends_with_l = 0
        self._ends_with_l = 1
        self._has_a_ends_with_ll = 0
        self._ends_with_ll = 0
        self._ends_with_a = 1

    def __len__(self):
        """Returns the number of valid records.

        :returns: The number of valid records.
        :rtype: int.
        """
        return self._has_a_ends_with_p + \
               self._ends_with_p + \
               self._has_a_ends_with_l + \
               self._ends_with_l + \
               self._has_a_ends_with_ll + \
               self._ends_with_ll + \
               self._ends_with_a

    def _make_next(self):
        """Creates the next record in the sequence.

        :returns: The next record in the sequence.
        :rtype: RecordStatus.
        """
        next_rec = RecordStatus()

        next_rec._has_a_ends_with_p = self._has_a_ends_with_p + \
                                      self._has_a_ends_with_l + \
                                      self._has_a_ends_with_ll + \
                                      self._ends_with_a

        next_rec._ends_with_p = self._ends_with_p + \
                                self._ends_with_l + \
                                self._ends_with_ll

        next_rec._has_a_ends_with_l = self._has_a_ends_with_p + \
                                      self._ends_with_a

        next_rec._ends_with_l = self._ends_with_p

        next_rec._has_a_ends_with_ll = self._has_a_ends_with_l

        next_rec._ends_with_ll = self._ends_with_l

        next_rec._ends_with_a = self._ends_with_p + \
                                self._ends_with_l + \
                                self._ends_with_ll
        return next_rec

    @classmethod
    def count(cls, length_of_record):
        """Counts the number of valid Student Attendance Records.

        :param int length_of_record: The size of the record.

        :return: The number of valid Student Attendance Records.
        :rtype: int.
        """
        status = RecordStatus()
        for _ in range(length_of_record - 1):
            status = status._make_next()
        return len(status)



def count_sequences(N):
    """A compact version of the solution.

    :param int N: The size of the record.

    :return: The number of valid Student Attendance Records.
    :rtype: int.
    """
    fs = 0
    fc = 0
    fcc = 0
    s = 1
    c = 1
    cc = 0
    f = 1

    n = 1
    while n < N:
        fs, fc, fcc, s, c, cc, f = (
            fs + fc + fcc + f,
            fs + f,
            fc,
            s + c + cc,
            s,
            c,
            c + s + cc
        )
        n += 1

    return fs + fc + fcc + s + c + cc + f
