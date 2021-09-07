def key_indexed_sort(data):
    """Sorts the passed in strings using key indexed method.

    :param List[(str, sector)] data: A list containing tuples of the
    the string to sort and its sector.

    :returns: A list with the sorted by sectors strings.
    :rtype: List[str]
    """
    max_sector = data[0][1]
    for _, sector in data:
        if sector > max_sector:
            max_sector = sector

    frequencies = [0] * (max_sector + 1)

    for _, sector in data:
        frequencies[sector] += 1

    for i in range(1, max_sector+1):
        frequencies[i] += frequencies[i-1]

    starting_position = [0] * (max_sector + 1)
    for i in range(1, max_sector + 1):
        starting_position[i] = frequencies[i-1]

    sorted_strings = [None] * len(data)
    for string, sector in data:
        sorted_strings[starting_position[sector]] = (string, sector)
        starting_position[sector] += 1

    return sorted_strings