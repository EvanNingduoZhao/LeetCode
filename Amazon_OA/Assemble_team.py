def assemble_team(skills,minAssociates, minLevel, maxLevel):
    count = 0
    def fact(n,r):
        nominator = 1
        for i in range(1,n+1):
            nominator*=i
        denominator = 1
        for i in range(1,r+1):
            denominator*=i
        for i in range(1,n-r+1):
            denominator*=i
        return int(nominator/denominator)
    for s in skills:
        if s>=minLevel and s<=maxLevel:
            count+=1
    res = 0
    for i in range(minAssociates,count+1):
        res+=fact(count,i)
    return res

skills = [12,4,6,13,5,10]
minAssociates = 3
minLevel = 4
maxLevel = 10
print(assemble_team(skills,minAssociates,minLevel,maxLevel))