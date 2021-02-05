def matrixQuery(n,m,queries):
    minRow=1
    minCol=1
    banned=set()
    res=[]
    for query in queries:
        if len(query)==1:
            while (1,minRow) in banned:
                minRow+=1
            while (2,minCol) in banned:
                minCol+=1
            res.append(minRow*minCol)
        else:
            if query[0]==1:
                banned.add((1,query[1]))
            else:
                banned.add((2,query[1]))
    return res

queries=[[0],[1,2],[0],[2,1],[0],[1,1],[0]]
res=matrixQuery(3,4,queries)
print(res)