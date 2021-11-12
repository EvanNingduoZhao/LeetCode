# An Amazon Fulfillment Associate has a set of items that need to be packed into two
# boxes. Given an integer array of the item weights (arr) to be packed, divide the item
# weights into two subsets, A and B, for packing into the associated boxes, while
# respecting the following conditions:
# The intersection of A and B is null.
# The union A and B is equal to the original array.
# The number of elements in subset A is minimal.
# The sum of A's weights is greater than the sum of B's weights.
# Return the subset A in increasing order where the sum of A's weights is greater than the
# sum of B's weights. If more than one subset A exists, return the one with the maximal
# total weight.

# 先从大到小sort，从重量最大的开始依次往setA里放，直到setA总重量超过所有box总重量的一半
def optBox(nums):
    nums.sort(reverse=True)
    halfTotalWeight = sum(nums)/2
    currSum = 0
    setA = []
    for box in nums:
        currSum+=box
        setA.append(box)
        if currSum>halfTotalWeight:
            break
    return setA[::-1]
print(optBox([4, 5, 2, 3, 1, 2]))
