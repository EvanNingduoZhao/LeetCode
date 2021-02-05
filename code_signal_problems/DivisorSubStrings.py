# divisorSubstrings
# Give a number n and digit number k find all serial substring is able to divisible n.
# Input: n = 120, k = 2
# Output: 2
# Explain:
# 120 -> 12 and 20
# 120 % 12 == 0 (O)
# 120 % 20 == 0 (O)
#
# Input: n = 555, k = 1;
# Output: 1
# Explain:
# 555 -> 5, 5 and 5 (Duplicate so only count one 5)
# 555 % 5 == 0 (O)
#
# Input: n = 2345, k = 2
# Output: 0
# Explain:
# 2345 -> 23, 34, 45
# 2345 % 23 != 0 (X)
# 2345 % 34 != 0 (X)
# 2345 % 45 != 0 (X)
#
# Time: O(n)
# 这道题就是问再n这个数字转化成的string里，有几个unique的长度为k的substring代表的数字是可以整除n的
# 这里substring必须连续的
def divisorSubStrings(n,k):
    start=0
    qualified=set()
    while start<len(str(n))-k+1:
        candidate=int(str(n)[start:start+k])
        if n%candidate==0:
            if candidate not in qualified:
                qualified.add(candidate)
                # print(qualified)
        start+=1
    return len(qualified)

print(divisorSubStrings(2345,2))