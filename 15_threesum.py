遍历list每个element都做一次第一个数，同时用twoSum的two pointers technique找到之和为第一个数的相反数的pair O(square of n)
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]

    """
    # check the extreme cases to be more robust
    if len(nums) < 3 or not nums:
        return []

    else:
        result = []
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        for i in range(n - 2):
            # since all the elements after sorted_nums[i] is greater or equal to sorted_nums[i]
            # three positive numbers can never have sum of 0
            if sorted_nums[i] > 0:
                break
            # if sorted_nums[i]= sorted_nums[i-1] then we will have duplicates
            # the rest is basically two pointers technique with some modifications to avoid duplicates
            if i == 0 or sorted_nums[i] > sorted_nums[i - 1]:
                start = i + 1
                end = n - 1
                while (start < end):
                    if sorted_nums[start] + sorted_nums[end] < 0 - sorted_nums[i]:
                        # also avoiding duplicates
                        currentstart = start
                        while sorted_nums[start] == sorted_nums[currentstart] and start < end:
                            start = start + 1
                    elif sorted_nums[start] + sorted_nums[end] > 0 - sorted_nums[i]:
                        currentend = end
                        while sorted_nums[end] == sorted_nums[currentend] and start < end:
                            end = end - 1
                    else:
                        result.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                        while (start < end and sorted_nums[start] == sorted_nums[start + 1]):
                            start = start + 1
                        while (start < end and sorted_nums[end] == sorted_nums[end - 1]):
                            end = end - 1

                        start = start + 1
                        end = end - 1

        return result


nums = [-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1]

print(threeSum(nums))

