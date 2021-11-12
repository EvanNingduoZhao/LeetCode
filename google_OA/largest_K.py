def largest_K(nums):
    indexPlusValue = {}
    indexMinusValue = {}
    maxK = 0
    for i in range(len(nums)):
        if i+nums[i] in indexPlusValue:
            maxK = max(maxK, i-indexPlusValue[i+nums[i]])
        else:
            indexPlusValue[i+nums[i]]=i
    for i in range(len(nums)):
        if i-nums[i] in indexMinusValue:
            maxK = max(maxK, i-indexMinusValue[i-nums[i]])
        else:
            indexMinusValue[i-nums[i]]=i
    return maxK

nums = [100]
print(largest_K(nums))