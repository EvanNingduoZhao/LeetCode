#Binary Search实际上就是很基础的，在input是一个sorted array的前提下，
# 查找某一个target element在不在input array中，首先用target和这个sorted array的mid element比较，
# 如果target更大，那就砍掉array的first half，在后一半里继续，如果target更小，就砍掉array的后一半，
# 在前一半里继续，如果target正好等于mid element，那就直接return mid element的index。
def binary_search(nums,target):
    #用start和end来控制砍input的操作
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        #如果target正好等于mid element，那就直接return mid element的index
        if nums[mid]==target:
            return mid
        #如果target更大，那就砍掉array的first half，在后一半里继续
        elif nums[mid]<target:
            start=mid+1
        #如果target更小，就砍掉array的后一半，在前一半里继续
        else:
            end=mid-1
    return -1

import random
if __name__ == "__main__":
    randomlist = random.sample(range(0, 200), 100)
    print(randomlist)
    print(binary_search(randomlist,111))