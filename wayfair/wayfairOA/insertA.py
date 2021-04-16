def insertA(s):
    if not s:
        return -1
    if len(s)==0:
        return 2
    res=0
    consecuACount=0
    for i in range(0,len(s)):
        if s[i] == 'a':
            consecuACount+=1
            if consecuACount==3:
                return -1
        if s[i] != 'a':
            res+=2-consecuACount
            consecuACount=0
    return res+2-consecuACount

inputStirngs=['aabab','dog','aa','baaaa']
for s in inputStirngs:
    print(insertA(s))
