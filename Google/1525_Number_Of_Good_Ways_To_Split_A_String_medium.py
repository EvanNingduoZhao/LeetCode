# 这道题就是只有一个memoization
# bruteforce就是用每个s里的char都做一次分界点，把分界点左边的traverse一下算有几个distinct的
# 再对分界点右边的做同样的事，看两侧distinct的数量是否一致，如果是就把numOfWays加1
# 但是这样重复查看很多，所以我们用两个dp list，第一个list里dp[i]里存着s[:i+1]里有多少个distinct
# 的字母，第二个list dp[i]里存着s[i:]里有多少个distinct字母
# 这样建好了两个dp list以后，同时traverse两个list，如果prevDistinctCount[i-1]==afterDistinctCount[i]
# 就把numOfWays加1

# 这道题的思考思路是这样的，观察后可以发现，就算我们知道整个s里有多少个distinct 的字母
# 在只知道s[:i]里有多少个distinct字母的情况下，如果不traverse s[i:]这部分，我们还是
# 不知道s[i:]有多少个distinct 字母。因此可以断定这道题没法通过subproblem之间的关系来用上
# 第二板斧，只能用memoization这第一板斧了。在知道只能用memoization之后，就要开始像蛮力办法
# 观察蛮力办法里什么地方是重复计算的，那就用memoization来存什么
class Solution:
    def numSplits(self, s: str) -> int:
        if len(s)==1:
            return 0
        prevSet = set(s[0])
        prevDistinctCount =[0 for _ in range(len(s))]
        prevDistinctCount[0]=1
        for i in range(1,len(s)):
            if s[i] not in prevSet:
                prevDistinctCount[i]=prevDistinctCount[i-1]+1
            else:
                prevDistinctCount[i]=prevDistinctCount[i-1]
            prevSet.add(s[i])
        afterSet = set(s[-1])
        afterDistinctCount =[0 for _ in range(len(s))]
        afterDistinctCount[-1]=1
        for i in range(len(s)-2,-1,-1):
            if s[i] not in afterSet:
                afterDistinctCount[i]=afterDistinctCount[i+1]+1
            else:
                afterDistinctCount[i]=afterDistinctCount[i+1]
            afterSet.add(s[i])
        numOfWays = 0
        for i in range(1,len(prevDistinctCount)):
            if prevDistinctCount[i-1]==afterDistinctCount[i]:
                numOfWays+=1
        return numOfWays

# 第二种办法是自己写的，属于不那么标准的dp，但是也是efficient的，不用看了
class Solution:
    def numSplits(self, s: str) -> int:
        pMap = {}
        for char in s:
            if char not in pMap:
                pMap[char]=1
            else:
                pMap[char]+=1
        qMap = {}
        numOfWays=0
        for i in range(len(s)-1,-1,-1):
            pMap[s[i]]-=1
            if pMap[s[i]]==0:
                pMap.pop(s[i])
            if s[i] not in qMap:
                qMap[s[i]]=1
            else:
                qMap[s[i]]+=1
            if len(pMap.keys())==len(qMap.keys()):
                numOfWays+=1
            if len(qMap.keys())>len(pMap.keys()):
                break
        return numOfWays