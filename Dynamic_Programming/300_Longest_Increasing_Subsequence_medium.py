#以下是这道题用Dynamic Programming的解法，time complexity是O(n^2)
#这道题最好解法是O(nlog(n))的time complexity, 等下会加在下面
#这道题跟Dynamic Programming在Notability里用来介绍DP的基本思路的那部分note里介绍的那道题的思路是一摸一样的
#只不过那道题要的是non-decreasing subsequence,这里要的是increasing subsequence
#复习这道题之前应该先看那篇笔记，关于思路在那篇笔记里写得已经很全了，这里的comment我就主要focus在代码实现上了
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #因为下面的j要从index 1开始，要求nums必须有两个及以上的elements
        #因此nums里只有一个element的情况也需要作为edge case特殊处理
        if len(nums)==1:
            return 1
        #用record这个list来记录以每个element为结尾的longest increasing subsequence的长度
        #例如record[i]的值就是以nums[i]这个item为结尾的longest increasing subsequence的长度
        #像note里说的一样，每个element itself至少都是一个长度为1的increasing subsequence
        #因此record的里的每个value的default value都是1
        record=[1 for _ in range(len(nums))]
        #这里的i和j就是遵循note里的i和j，注意针对一个j，我们要把在它前面的所有item都作为i尝试
        #一下，看看nums[j]能不能被append在以nums[i]为结尾的longest increasing subsequence后面
        #形成一个更长的increasing subsequence，因此在traverse j前面的所有i时，record[j]的value是
        #会可能被不断更新成一个更大的值的，知道traverse完j前面的所有item我们才能确定record[j]最后的正确值
        for j in range(1,len(nums)):
            for i in range(0,j):
                #因为题目中要的是increasing subsequence,那么首先nums[j]必须比nums[i]大
                #num[j]才能够被append在以nums[i]为结尾的longest increasing subsequence的后面
                #形成一个更长的increasing subsequence。
                #其次，只有以nums[i]为结尾的longest increasing subsequence的长度,即record[i]大于等于
                #现在record[j]的值，那么让record[j]=record[i]+1才能让record[j]等于一个更大的值
                if nums[i]<nums[j] and record[i]>=record[j]:
                    record[j]=record[i]+1
        return max(record)