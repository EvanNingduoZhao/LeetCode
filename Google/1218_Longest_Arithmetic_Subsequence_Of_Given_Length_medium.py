# 这道题还是属于和300 longest increasing subsequence同一个类型的
# 注意：因为问的是subsequence所以不能sort
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        # 一个num至少自己是一个length为1的arithmetic subsequence
        longestArithSub = 1
        for num in arr:
            if num-difference in dp:
                dp[num]=dp[num-difference]+1
            # 如果num-difference不在num左边的elements中，那么还是要
            # 把num：1放到map里去
            else:
                dp[num]=1
            longestArithSub = max(longestArithSub,dp[num])
        return longestArithSub