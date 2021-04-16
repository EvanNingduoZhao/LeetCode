def balloon(s):
    counter={}
    charList = ['B', 'A', 'L', 'O', 'N']
    for char in s:
        if char in charList:
            if char not in counter:
                counter[char]=1
            else:
                counter[char]+=1
    res=float('inf')
    for char in charList:
        if char not in counter:
            return 0
        if char=='L' or char=='O':
            res=min(res,counter[char]//2)
        else:
            res=min(res,counter[char])
    return res

s=""
print(balloon(s))