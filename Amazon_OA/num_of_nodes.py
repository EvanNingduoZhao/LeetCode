def num_of_nodes(matrix):
    curr  =0
    prev = 0
    res=0
    for r in matrix:
        for c in matrix[r]:
            if matrix[r][c]==1:
                curr+=1
        # curr != 0, prev=0
        # curr !=0, prev!=0
        # curr =0
        res+=curr*prev
        if curr!=0:
            prev=curr
    return res