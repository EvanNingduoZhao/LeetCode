def reassignPriority(arr):
    arrCopy = arr[:]
    arrSorted = list(set(arrCopy))
    arrSorted.sort()
    indexDict = {}
    for i in range(len(arr)):
        if arr[i] in indexDict:
            indexDict[arr[i]].append(i)
        else:
            indexDict[arr[i]]=[i]
    for i in range(len(arrSorted)):
        for j in indexDict[arrSorted[i]]:
            arrCopy[j]=i+1
    return arrCopy

print(reassignPriority([1,4,8,4]))
