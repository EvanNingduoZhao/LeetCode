#想要完成这个任务，我们必须变iterate through这个array边记录我们看到了什么
#难点在于： 不让用extra memory怎么记录？
#题干的重要信息是所有的elements都在1和n的区间内，n是array的length。
#想到办法：没看到一个新的element num就把array[num-1]那个element变成负的
#这样不会lose info因为只是变负，值还在就够了
#因为所有element都是在1和n的区间里，所有index是够的
#array过了一遍以后，第二遍过，看到那个element还是正的就把它的index+1放到ans里面


class Solution:
    def findDisappearedNumbers(nums):
        for num in nums:
            if num<0:
                num=-num
            if nums[num-1]>0:
                nums[num-1]=-nums[num-1]

        ans=[]
        for i in range(0,len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans

    test=[4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(test))