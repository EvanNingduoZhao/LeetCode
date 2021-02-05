# 第一个是自己写的time是O（N^2）的solution，第二个是使用了KMP_algorithm的time是O(N)的solution
def prefixSubstring(s):
    start=0
    end=1
    longestEnd=0
    newEnd=0
    while start<len(s):
        while end<len(s):
            if s[end]==s[start]:
                l=start
                r=end
                while l<=r:
                    if s[l]==s[r]:
                        l+=1
                        r-=1
                    else:
                        break
                if l>r:
                    newEnd=end
                    print('palindrom found',s[start:newEnd+1])
                    print(s[newEnd+1:])
            end+=1
        if newEnd==longestEnd:
            if newEnd==0:
                return s
            else:
                return s[newEnd+1:]
        else:
            longestEnd=newEnd
            start=longestEnd+1
            end=start+1
    return ""

# print(prefixSubstring('aaacodedoc'))
# print(prefixSubstring('codesignal'))
# print('just returned')

def Helper(s):
    temp=s+'?'
    # 我们这里把input的string后面先加上一个？再加上自己的倒序，把结果叫temp
    # 那么对于temp而言，既是最长的suffix的又是prefix的substring就一定是最长的palindrom了
    # 因此我们这里用KMP的preprocessing的思想，来找这个最长的既是suffix的又是prefix的substring
    temp+=s[::-1]
    n=len(temp)
    lps=[0]*n
    for i in range(1,n):
        Len=lps[i-1]
        while (Len>0 and temp[Len]!=temp[i]):
            Len=lps[Len-1]
        if temp[Len]==temp[i]:
            # 这里实际上也是起头并进，只不过i的incremnt是由for loop完成的
            Len+=1
        lps[i]=Len
    return lps[n-1]

def prefixSubstring(s):
    if len(s)<2:
        return s
    plen=Helper(s)
    if plen<2:
        return s
    else:
        # print(s[plen:])
        return prefixSubstring(s[plen:])

print(prefixSubstring('codedocaaa'))



