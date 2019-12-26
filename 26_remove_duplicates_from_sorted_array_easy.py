
#本题要求的是不能新建一个array 所以下面的自己写的方法其实是违规的
#答案方法用的是快慢双指针，i是慢的，j是快的
#如果nums[j]=nums[i] 那么说明j处的是和前面的重复的，for loop继续j+1
#如果nums[j]！=nums[i] 那么说明j处的是和前面的不是重复的，那就把i+1处的数字换成j处的数字（就算现在j仅仅是i的紧后面一个也没事）
#注意 nums[i]永远是没有duplicate的subarray的最后一个 所以new length是i-1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:
            return length
        else:
            i=0
            for j in range(length):
                if (nums[i]!=nums[j]):
                    i+=1
                    nums[i]=nums[j]
        return i+1
############################################################

    def removeDuplicates_my_own_attempt(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:
            return length
        else:
            counter=0
            queue = []
            dict = {}
            for i in range(length):
                if nums[i] in dict:
                    queue.append(i)
                else:
                    counter+=1
                    dict[nums[i]]=i
                    if len(queue)!=0:
                        nums[queue.pop(0)]=nums[i]
                        queue.append(i)
        return counter