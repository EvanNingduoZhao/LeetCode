#本题自己的方法用的是左右双指针，这样写起来比较麻烦
#答案用的是快慢双指针，写起来简洁明了
#这种in place modify array的题目就是要用快慢指针，快的在前面一个一个筛查，找到应该keep的
#慢的在后面记录现在前一个是已经弄好的，时刻准备接住快的指针在前面找到的新的该keep的

class Solution:
    def removeElement(nums, val):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            if nums[0]==val:
                nums.pop(0)
                return 0
            else:
                return 1
        else:
            i=0
            for j in range(len(nums)):
                if nums[j]!=val:
                    nums[i]=nums[j]
                    i+=1
        return i+1

    list=[3,2,2,3]
    print(removeElement(list,3))
    print(list)
#########################################################
    def removeElement_my_own_solution(nums, val):
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            if nums[0]==val:
                nums.pop(0)
                return 0
            else:
                return 1
        else:
            left=0
            right=len(nums)
            while(left<right):
                if nums[left]==val:
                    right-=1
                    while(nums[right]==val and right > left):
                        right-=1
                    if nums[right]==val:
                        left-=1
                    else:
                        nums[left]=nums[right]
                left+=1
            return left