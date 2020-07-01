
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #根据harmonious subsequence的定义，一个list里必须至少有两个element才有可能有一个
        # harmonious subsequence
        if not nums or len(nums)<2:
            return 0
        else:
            record={nums[0]:1}
            res=0
            for num in nums[1:]:
                #边traverse 边用dict记录每个value出现了多少次
                if num in record:
                    record[num]+=1
                else:
                    record[num]=1
                #每次碰见完一个新的element，看看num+1 或者num-1都有没有在list里出现过
                #出现过几次
                #出现过的话算出来num和这个num+1或者num-1一共出现过几次
                #和目前最长的harmonious subsequence比谁大，大就update
                if num+1 in record:
                    length1=record[num]+record[num+1]
                    res=max(res,length1)
                if num-1 in record:
                    length2=record[num]+record[num-1]
                    res=max(res,length2)
            return res