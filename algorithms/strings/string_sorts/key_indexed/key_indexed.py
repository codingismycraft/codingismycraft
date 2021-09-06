

def key_indexed_sort(data, min_sector, max_sector):
    """Sorts the passed in strings using key indexed method.

    :param list[Tuple[str, int]] data: A list of tuples consisting of a string
        and a section to sort by.
    """

    sector_frequency = [0] * (max_sector + 1)

    for student in data:
        sector_frequency[student.sector] += 1

    index_for_sector = [0] * (max_sector + 1)

    current_index = 0
    for index, frequency in enumerate(sector_frequency):
        index_for_sector[index] = current_index
        current_index += frequency

    sorted_students = [""] * len(data)

    for student in data:
        position = index_for_sector[student.sector]
        sorted_students[position] = student
        index_for_sector[student.sector] += 1

    return sorted_students
