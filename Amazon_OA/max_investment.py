def maxValue(n,rounds):
    assets = [0]*n
    maxValue = 0
    for round in rounds:
        left = round[0]
        right = round[1]
        contrib = round[2]
        for i in range(left-1,right):
            assets[i]+= contrib
            maxValue = max(maxValue, assets[i])
    return maxValue

contributions = [[1,2,10],[2,4,5],[3,5,12]]
print(maxValue(5,contributions))
