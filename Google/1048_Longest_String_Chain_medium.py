# 本题找思路流程：
# 1. 要找的组合内部的元素之间需要满足一些条件，不是背包
# 2. 要length of the longest possible word chain, 属于找最优解问题
# 3. 一个word只有可能被append到长度等于自己长度-1的word后面形成chain，按照word length sort list
# 4. 确定本题跟300 longest increasing sub sequence属于同一类型（300问的是subsequence所以不能sort）
# 这道题问的不是subsequence所以可以sort
# 5. 想明白到底一个新遇到的word要满足什么条件才能被append到一个已经遇到过的word后面形成chain

# 这道题实际上和300 longest increasing sub sequence很像
# 都需要先把list从小到大sort一下，保证一个element只能append到它左面的element后面
# 这道题稍微更难了一层，300是一个新遇到的element一定可以append到任何一个它左面的element
# 后面（因为新element一定是大于等于它左边的elements的）但是这道题需要尝试把新遇到的word
# 里面每个位置上的char都删掉一次，看得到的newWord是不是在一个我们左边已经遇到过的words之中
# 如果是新遇到的word才能append人家后面。但是除了这一点小区别外其余思路完全一样
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        #先把words这个list按照element的length来从小到大sort
        # 这样保证了一个新碰到的word只能作为它左边的words（也就是我们已经都看到过的words）
        # 的successor
        words.sort(key=lambda x:len(x))
        dp = {}
        # 记录在我们已经见到过的所有chain中最长的的长度，因为一个word最差也可以自己作为一个
        # 长度为1的chain
        globalLongestChain = 1
        # 对于sort过后的list里的每一个word
        for word in words:
            # 记录以这个word为结尾的chain的最长的长度能是多少
            longestChain = 1
            # 尝试通过把word里的每一个位置的上的char删掉，form一个新word
            # 比如word是abc，那么我们一共要尝试的就是ab，ac，bc
            for i in range(len(word)):
                newWord = word[:i]+word[i+1:]
                # 如果这个通过把原word A里一个char删掉得到的newWord是和我们之前在list中
                # 已经遇到过的一个word B是一样的，那么说明word A是可以作为word B的successor
                # 来本append到原本以word B作为结尾的chain后面的
                if newWord in dp:
                    # 因此以word A结尾至少可以form一个长度等于（以word B结尾的最长的
                    # chain的长度）+1的chain
                    chainLength = dp[newWord]+1
                    # 更新已知的以word A结尾的chain最长的长度
                    longestChain = max(longestChain,chainLength)
                    # 更新已知所有chain中最长的长度
                    globalLongestChain = max(globalLongestChain,chainLength)
            # 在尝试过把wordA里的每一个位置的char都删除一次后，把新的key value pair
            # 放到map里，key是word A，value是以wordA结尾的chain的最长长度
            dp[word]=max(1, longestChain)
        return globalLongestChain