#这道题应该这样分割subproblem，我们用两个pointer，i和j，i要从0 iterate到len(s)-1， 那么s[0：i]就是我们目前在
#work with的substring，对于这个substring，我们用j从0iterate到i-1，在这里j把s[0:i]进一步分成两个sub-substring
#即s[0:j]和s[j+1:i]，如果第二个subtring s[j+1:i]是一个在wordDict里的单词的话，那么只要第一个substring s[0:j]
# 能够被完全分割成wordDict里的字母的话，那么s[0:i]这个大substring就也可以被分割成全部都在wordDict里的词。而在此前
# i已经走过当前j所在的位置了，如果我们已经知道s[0:j]的答案了，因此只需要check dp[j]是多少就好了，当然之后还要更新一下
# dp[i]. 此方法时间是O(n^3)因为i和j是nested for loop这就是n^2，但是每次还有一个取substring的操作，这又是take n所以
# 一共是n^3，空间就是O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False for _ in range(0, len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] == True and s[j:i] in wordSet:
                    dp[i] = True
        return dp[-1]