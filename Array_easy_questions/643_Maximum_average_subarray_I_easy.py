#想找到最大的平均值就要找到最大的和
#那么最简便的方式即，iterate through 这个array，往current里加上最新看到的elemen同时减去k个之前的哪个element
#将得到的current和目前为止的max比较，最后return max/k
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max=0
        current=0
        for j in range(0,k):
            max+=nums[j]
            current+=nums[j]
        for i in range(k,len(nums)):
            current=current+nums[i]-nums[i-k]
            if current>max:
                max=current
        return max/k