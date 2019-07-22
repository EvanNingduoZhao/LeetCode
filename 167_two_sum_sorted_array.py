# we categorize this problem as searching for pairs in sorted arrays. hash and two pointers are both O(n). this time we introduce two pointers:
# 对于sorted arrays先取最左和最有两个极端值，如果两者之和小于target，那最小的和最大的相加都不够target => 最小的和其他小于max的elements相加就更不够了，因此排除min在wanted pair中的可能=>left index+1 同理两数之和大于target的话就把 right index-1


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
        while left < right:
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
