"""Brutal solution of the Student Attendance Record Problem."""

def count_valid_records_brutal(length_of_record):
    """Brutal solution of the Student Attendance Record Problem.

    :param int length_of_record: The size of the record.

    :return: The number of valid Student Attendance Records.
    :rtype: int.
    """
    records = ['P', 'L', 'A']
    for i in range(1, length_of_record):
        new_records = []
        for record in records:
            for c in 'PLA':
                new_str = record + c
                if 'LLL' in new_str or new_str.count('A') >= 2:
                    continue
                new_records.append(new_str)
        records = new_records
    return len(records)

