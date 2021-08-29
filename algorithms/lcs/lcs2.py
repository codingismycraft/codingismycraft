def lcs(s1,s2):
    table=[]


    for row in range(0,(len(s1)+1)):
        table.append([0]*(len(s2)+1))
    for row in range(1,len(s1)+1):
        char_1=s1[row-1]
        for col in range(1,len(s2)+1):
            char_2=s2[col-1]
            if char_2==char_1:
                table[row][col]=table[row-1][col-1]+1
            else:
                v1=table[row][col-1]
                v2=table[row-1][col]
                table[row][col]=max(v1,v2)
    return table[-1][-1]

