# 对于00110011这个input而言，其实我们可以把它分成00，11，00，11这四组，那么第一组和第二组在一起即0011可以组合出两个来
# 即0011和01，注意能组合出两个其实是这么来的：min(第一组的长度，第二组的长度)，比如如果是111100，那么也只能组合出两个
# 之后再看第二组和第三组能组合出几个，以此类推。
class Solution:

    def countBinarySubstrings(self, s: str) -> int:
        prevGroup = 0
        currGroup = 1
        res=0
        for i in range(1,len(s)):
            # 如果当前的和上一个一样，那么我们还在看同一组的，给这组的长度再加一
            if s[i]==s[i-1]:
                currGroup += 1
            # 如果当前和上一个不一样了，那么说明我们再看下一组了
            # 按照00110011的例子，当前再第三个0时，prevGroup是00，currGroup是11
            # 因此往res上加2，之后让prev=curr，新的curr=1
            else:
                res+=min(prevGroup, currGroup)
                prevGroup=currGroup
                currGroup=1
        # 注意return之前即在00110011里走到最后一个1了，那么prev是00，curr是11，这时还是要把最后一个2加到res上
        return res+min(prevGroup,currGroup)