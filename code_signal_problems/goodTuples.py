# Give an array and find the count of a pair number and a single number combination in
# a row of this array. Target array is a[i - 1], a[i], a[i + 1]
# Input: a = [1, 1, 2, 1, 5, 3, 2, 3]
# Output: 3
# Explain:
# [1, 1, 2] -> two 1 and one 2(O)
# [1, 2, 1] -> two 1 and one 2(O)
# [2, 1, 5] -> one 2, one 1 and one five(X)
# [1, 5, 3] -> (X)
# [5, 3, 2] -> (X)
# [3, 2, 3] -> (O)
# 三个数字里有两个数字是一样的，一个是和另外两个不一样的就算
# Time: O(n)

def goodTuples(arr):
    start=0
    res=0
    while start<len(arr)-2:
        seen=set()
        for i in range(0,3):
            if arr[start+i] in seen:
                continue
            else:
                seen.add(arr[start+i])
        if len(seen)==2:
            res+=1
        start+=1
    return res

arr=[1,1,2,1,5,3,2,3]
print(goodTuples(arr))