def coolFeature(a,b,queries):
    aContent=set(a)
    res=[]
    for query in queries:
        if len(query)==2:
            count=0
            for num in b:
                if query[1]-num in aContent:
                    count+=1
            res.append(count)
        else:
            b[query[0]]=query[1]
    return res

query=[[1,5],[1,1,1],[1,5]]
print(coolFeature([1,2,3],[3,4],query))