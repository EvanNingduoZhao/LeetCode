import math
def bucket_sort(nums):
    minimum=maximum=0
    for num in nums:
        minimum=min(minimum,num)
        maximum=max(maximum,num)
    #这里我们assume 用10个bucket
    #又ceil的原因是81一个元素装到10个桶里，每个桶得装8+1等于9个才能装下
    bucket_size=math.ceil((maximum-minimum+1)/10)
    # buckets是一个list of empty lists
    buckets=[[] for _ in range(10)]
    # 把inputlist里的元素挨个放到自己该去的bucket里
    for num in nums:
        buckets[(num//bucket_size)].append(num)

    # 一个insertion sort的helper function
    def __insertion_sort(nums):

        def __swap(nums,i,j):
            nums[i],nums[j]=nums[j],nums[i]

        for i in range(1,len(nums)):
            j=i
            while j>0 and nums[j]<nums[j-1]:
                __swap(nums,j,j-1)
                j-=1
        return nums

    # 由于这里我们想直接改变inputlist，最后也return nums
    # 所以我们用index来keep track我们目前在nums里的位置
    # 把sort好的bucketet里的每一个元素挨个放到nums[index]上，在increment index
    index=0
    for bucket in buckets:
        # bucket里没东西直接跳过
        if len(bucket)==0:
            continue
        # bucket里只有一个元素 不用sort直接放到nums[index]上
        elif len(bucket)==1:
            nums[index]=bucket[0]
            index+=1
        # bucket里多于一个元素的话 insertion sort好以后再挨个放到nums里
        else:
            for num in __insertion_sort(bucket):
                nums[index]=num
                index+=1
    return nums

import random
if __name__ == "__main__":
    randomlist = random.sample(range(0, 900), 100)
    print(randomlist)
    bucket_sort(randomlist)
    print(randomlist)