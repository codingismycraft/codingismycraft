def key_indexed_sort(data, min_sector, max_sector):
    """Sorts the passed in strings using key indexed method.

    :param list[Tuple[str, int]] data: A list of tuples consisting of a string
        and a section to sort by.
    """
    # sectors = [d[1] for d in data]
    # min_sector = min(sectors)
    # max_sector = max(sectors)

    assert min_sector > 0
    assert max_sector > min_sector

    sector_frequency = [0 for _ in range(0, max_sector+1)]

    for _, sector in data:
        sector_frequency[sector] += 1

    index_for_sector = [0 for _ in range(0, max_sector+1)]

    current_index = 0
    for index, frequency in enumerate(sector_frequency):
        index_for_sector[index] = current_index
        current_index += frequency

    sorted_strings = [None for _ in range(len(data))]

    for string, sector in data:
        position = index_for_sector[sector]
        sorted_strings[position] = string
        index_for_sector[sector] += 1

    return sorted_strings







