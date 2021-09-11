# // Given an array of integers, determine the number of ways the entire array be split into two non-empty subarrays, left and right, such that the sum of elements in the left subarray is greater than the sum of elements in the right subarray.
# #
# # // Example
# # // arr =  [10, 4, -8, 7]
# # // There are three ways to split it into two non-empty subarrays:
# # // [10] and [4, -8, 7], left sum = 10, right sum = 3
# # // [10, 4] and [-8, 7], left sum = 10 + 4 = 14, right sum = -8 + 7 = -1
# # // [10, 4, -8] and [7], left sum = 6, right sum = 7
# # // The first two satisfy the condition that left sum > right sum, so the return value should be 2.

def splitIntoTwo(nums):
    halfTotal = sum(nums)/2
    currSum = 0
    res = 0
    for num in nums[:-1]:
        currSum+=num
        if currSum>halfTotal:
            res+=1
    return res

print(splitIntoTwo([10,4,-8,7]))