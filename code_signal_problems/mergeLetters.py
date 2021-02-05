def mergeletters(s,t):
    if not s or len(s)==0:
        return t
    if not t or len(t)==0:
        return s
    res=''
    index=0
    while index<len(s) and index < len(t):
        res+=s[index]
        res+=t[index]
        index+=1
    while index<len(s):
        res+=s[index]
        index+=1
    while index<len(t):
        res+=t[index]
        index+=1
    return res

print(mergeletters('aaaaa','bbb'))
print(mergeletters('ab','abcdef'))