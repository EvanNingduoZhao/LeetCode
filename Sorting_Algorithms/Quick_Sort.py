#以下code是参照这个视频写的
# https://www.youtube.com/watch?v=CB_NCoxzQnk

def quick_sort(nums):
    __quick_sort(nums,0,len(nums)-1)

# 这个helper function的左右是user不需要输入low和high这些paramter，输入要sort的list就好了
def __quick_sort(nums,low,high):
    if low<high:
        pivot=__partition(nums,low,high)
        __quick_sort(nums,low,pivot-1)
        __quick_sort(nums,pivot+1,high)

# 这个helper是用来比较mid和low和high之间所指的elements的中位数是谁的，是谁就用谁做pivot
def __get_pivot(nums,low,high):
    # when the input sub-list only has 2 elements
    if high-low==1:
        return low
    # find the median among low,high and mid
    mid =(low+high)//2
    pivot=high
    if nums[low]<=nums[mid]:
        if nums[mid]<=nums[high]:
            pivot=mid
        else:
            if nums[low]<=nums[high]:
                pivot=high
            else:
                pivot=low
    else:
        if nums[low]<=nums[high]:
            pivot=low
    return pivot

def __swap(nums,i,j):
    nums[i],nums[j]=nums[j],nums[i]


def __partition(nums,low,high):
    pivotIndex=__get_pivot(nums,low,high)
    pivotValue=nums[pivotIndex]
    # 为了让后续的代码好写一些，我们先把pivotIndex指向的值swap到sublist的开头
    # 因为如果不这样的话，在two pointer traverse的时候有一个pointer碰到了pivotIndex
    # 的话还得跳过它
    __swap(nums,pivotIndex,low)
    #border一直指向最右侧的那个被j遇到并且扔回前面的小于pivotValue的element
    #也就是说border左边的所有elements，包括border自己都是小于pivotValue的
    border=low
    for j in range(low,high+1):
        if nums[j]<pivotValue:
            #这里想给border+1，让border指向第一个不小于pivotValue的Element
            border+=1
            #再swap border和j所指的elements
            __swap(nums,border,j)
        #Note：每次border刚被+1以后，就马上swap，swap之后border就又指向一个小于pivotvalue
        # 的element了，所以border在能被access的时候永远都是指向小于pivotValue那一部分
        # 的最右侧的那个element，因此j traverse完sublist以后直接swap low（pivotValue所在
        # 的地方）和border
    __swap(nums,low,border)
    return border



import random
if __name__ == "__main__":
    randomlist = random.sample(range(0, 900000), 100000)
    print(randomlist)
    quick_sort(randomlist)
    print(randomlist)