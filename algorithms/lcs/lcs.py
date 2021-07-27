def lcs(s1,s2):
    """Finds the longest common subsequence between two strings.

    :param str s1: The first of the two strings to be compared.
    :param str s2: The second string.

    :return: The length of the longest common subsequence.
    :rtype: int
    """
    table=[]
    num_rows=len(s1)+1
    num_cols=len(s2)+1
    for row_index in range(0,num_rows):
        table.append([0]*num_cols)
    for row_index in range(1,num_rows):
        char_1=s1[row_index-1]
        for col_index in range(1,num_cols):
            char_2=s2[col_index-1]
            if char_1==char_2:
                table[row_index][col_index]=table[row_index-1][col_index-1]+1
            else:
                v1=table[row_index-1][col_index]
                v2=table[row_index][col_index-1]
                table[row_index][col_index]=max(v1,v2)

    return table[-1][-1]