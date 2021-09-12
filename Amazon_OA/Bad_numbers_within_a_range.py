def goodSegment(badNumbers, lower, upper):
    badNumbers.sort()
    print("badNumber is:", badNumbers)
    # 用binary search 找到sorted badNumbers中第一个比lower大的数字
    start = 0
    end = len(badNumbers)-1
    while start < end:
        mid = start + (end-start)//2
        if badNumbers[mid]<lower:
            start = mid+1
        else:
            end = mid
    print("startBadNumber is:", badNumbers[start])
    # 如果badNumbers[start]的确是一个在lower和upper之间的数的话
    if badNumbers[start]>=lower and badNumbers[start]<=upper:
        maxDiff = badNumbers[start]-lower
        # 如果start不是badNumbers里的最后一个index
        if start!=len(badNumbers)-1:
            for i in range(start+1, len(badNumbers)):
                # 如果当前看到的badNumber[i]要大于upper，那么要把upper-badNumbers[i - 1]和现有的maxDiff比较一下
                if badNumbers[i]>upper:
                    maxDiff = max(maxDiff, upper - badNumbers[i - 1])
                    break
                maxDiff = max(maxDiff,badNumbers[i]-badNumbers[i-1])
                print("maxDiff is:", maxDiff)
        # 如过start就是badNumbers里的最后一个index，那上面的for loop用不了，要如下单独讨论
        else:
            maxDiff=max(badNumbers[start]-lower, upper-badNumbers[start])
        return maxDiff-1
    # 可能badNumbers里没有在lower和upper之间的数字，这种情况下我们要return upper-lower+1
    else:
        return upper-lower+1

badNumbers = [37, 7, 22, 15, 49, 60]
lower = 3
upper = 48
print(goodSegment(badNumbers, lower, upper))