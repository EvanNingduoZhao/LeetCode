# Question:
# An array is said to be analogous to the secret array if all of the following conditions are true:
#  The length of the array is equal to the length of the secret array.
#  Each integer in the array lies in the interval [lowerBound, upperBound].
#  The difference between each pair of consecutive integers of the array must be equal to the difference between the respective pair of consecutive integers in the secret array. In other words, let the secret array be [s[0], s[1],..., s[n-1]] and let the analogous array be [a[0], a[1],..., a[n-1]], then (a[i-1] - a[i]) must be equal to (s[i-1] - s[i]) for each i from 1 to n -1.
#
#  Given the value of integers lowerBound and upperBound, inclusive, and the array of differences between each pair of consecutive integers of the secret array, find the number of arrays that are analogous to the secret array. If there is no array analogous to the secret array, return 0.
#
#  For example:
#  consecutiveDifference = [-2, -1, -2, 5]
#  lowerBound = 3
#  upperBound = 10
#
#  Note that none of the values is out of the bound. All possible analogous arrays are:
#  [3, 5, 6, 8, 3]
#  [4, 6, 7, 9, 4]
#  [5, 7, 8, 10, 5]
#
#  The answer is 3.

# 解体思路 这道题问的是对于一个secret array而言，能有几个analogous array。因为analogous array每两个
# 相邻的num之间的差必须等于secret array每两个相邻item之间的差，
# 因此对于analogous array而言，只要确定了第一个数字，那么所有数字就都确定了
# 一系列consecutiveDiff一个个加到array的第一个数字上之后形成了array第一个后面的每一个数字
# 一个个consecutiveDiff的和也会造就最高的波峰和最低的波谷
# 我们的目标是保证start+highest <= upperBound, 且 start+lowest>=lowerBound
# 化简不等式后得到lowerbound - lowest <= start <= upperBound - highest
# 那么最终的结果就是看start可以有多少个取值，还要至于要check一下（upperBound - highest）是不是大于等于
# （lowerbound - lowest）否则return 0
def count_secret_pairs(upperBound, lowerBound, consecutiveDiff):
    sum = 0
    lowest = float("inf")
    highest = (-1)*float("inf")
    for diff in consecutiveDiff:
        sum+=diff
        if sum>highest:
            highest=sum
        if sum<lowest:
            lowest=sum
    startUpperBound = upperBound-highest
    startLowerBound = lowerBound-lowest
    if startUpperBound-startLowerBound >= 0:
        # 注意要+1
        return startUpperBound-startLowerBound+1
    else:
        return 0

print(count_secret_pairs(10,3,[-2, -1, -2, 5]))