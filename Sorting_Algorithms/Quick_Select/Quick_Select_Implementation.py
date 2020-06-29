# quick select实际上和quick sort是很相似的，quick select是用来求一个input里第k小或者第k大的element
# 问题的。原理是假设在有100个元素的inputlist里求第30小的元素是哪个，那么我们先用和quicksort一样的partition
# partition把pivot放到正确的位置后，如果pivot的index是大于30的，那么因为比pivot小的元素都在pivot左边
# 所以第30小的元素一定也在pivot左边，所以从此以后这个pivot右边的内容我们都不用管了，我们继续只partition
# pivot左边的所有元素，就这样不断一半一半砍掉第30小的元素不可能在的那一半。直到最后pivot的index就是落在
# 30为止。return pivot对应的值即可

# 这个implementation里求的是第k个，也就是只要这个1个
# 看Heap里的347题的quick select解法，里面讲的是怎么求前k个，也就是一共要k个
# 但是这种题能有quick select做的前提是，题中不要求在return这个k个的时候这k个也得按循序排列
#
import random
def quick_select(nums,k):

    def __swap(nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]

    def __partition(nums,low,high):
        pivot_index=random.randint(low,high)
        pivot_value=nums[pivot_index]
        __swap(nums,low,pivot_index)
        border=low
        for j in range(low+1,high+1):
            if nums[j]<pivot_value:
                border+=1
                __swap(nums,border,j)
        __swap(nums,border,low)
        return border


    def __quick_select(nums,low,high,k):
        pivot_index=__partition(nums, 0, len(nums) - 1)
        if pivot_index==k-1:
            return nums[pivot_index]
        elif pivot_index<k-1:
            return __quick_select(nums,pivot_index+1,high,k)
        else:
            return __quick_select(nums,low,pivot_index-1,k)

    return __quick_select(nums,0,len(nums)-1,k)


if __name__ == "__main__":
    input = [2, 8, 5, 3, 9, 4, 1]
    randomlist = random.sample(range(0, 10000), 10000)
    print(randomlist)
    print(quick_select(randomlist,954))