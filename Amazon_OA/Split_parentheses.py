# Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.
#
# Example 1:
#
# Input: nums = [1, 1, 2, 45, 46, 46], target = 47
# Output: 2
# Explanation:
# 1 + 46 = 47
# 2 + 45 = 47
# Example 2:
#
# Input: nums = [1, 1], target = 2
# Output: 1
# Explanation:
# 1 + 1 = 2
# Example 3:
#
# Input: nums = [1, 5, 1, 5], target = 6
# Output: 1
# Explanation:
# [1, 5] and [5, 1] are considered the same.

# 这道题所给的list没有sorted所以用hashset，因为题目中要unique的pairs的数量，所以我们要用另一个hashset of tuples来储存
# 已经发现的pair，这个hashset叫pairs，且规则是每个tuple都是小的数在前，大的数字在后，只有新发现的pair不在pairs里时才把它加进来
# 最后return pairs里tuple的数量

def split_parentheses(nums, target):
    pairs = set()
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            if complement > num:
                result = (num, complement)
            else:
                result = (complement, num)
            if result not in pairs:
                pairs.add(result)
        seen.add(num)
    print(pairs)
    return len(pairs)

nums = [1,5,1,5]
target = 6
print(split_parentheses(nums,target))