# we categorize this problem as searching for pairs in sorted arrays.
# hash and two pointers are both O(n). this time we introduce two pointers:
# 对于sorted arrays先取最左和最右两个极端值，如果两者之和小于target，
# 那最小的和最大的相加都不够target => 最小的和其他小于max的elements相加就更不够了，
# 因此排除min在wanted pair中的可能=>left index+1 同理两数之和大于target的话就把 right index-1
# 对于[2 7 11 15]这个list而言如果target是19的话，首先2+15小于19 那么左pointer+1，7+15大于19，
# 右pointer-1，这时候我们看到的是7+11。那么有一个问题，我们从来没看过2和11的组合，但是其实没问题
# 2和11不用看，因为2和15相加都小，那2和15左边的任何一个相加都不够，所以没必要看
#

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(numbers) < 2 or not numbers:
        return [-1, -1]
    else:
        left, right = 0, len(numbers) - 1
        #如果left和right错开了那就证明这个list里面没有目标组合
        while left < right:
            #能进来这个if的left和right已经都是被check过left<right的
            #所以不存在left=right的情况出现，可能经过下面的右减1或者左加1以后left会等于right
            #但是那样的话它们就进不来while loop了
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]


# hash
#         hashdict={}
#         for index,value in enumerate(numbers,start=0):
#             if target-value in hashdict:
#                 return [hashdict[target-value]+1,index+1]
#             else:
#                 hashdict[value]=index
#
#         return [-1,-1]

nums = [2,7,11,15]
print(twoSum(nums,9))
