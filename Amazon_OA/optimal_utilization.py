#  input: deviceCapacity = 7, foregroundAppList = [[1,2],[2,4],[3,6]],
#  backgroundAppList = [[1,2]]  数组里的第一个数算是index，第二个是value
#  output: 从f 和 b里面选出value和不超过deviceCapacity，尽量接近deviceCapacity 的组合的index，
#  上面的例子的结果是 [1,2]。
#  题不难，就是要注意是要求出所有组合，比如：
#  input: deviceCapacity=30, foregroundAppList = [[1,11],[2,11],[3,11]],
#  backgroundAppList = [[1,9],[2,9]]
#  返回的值是 [[1,1],[2,1],[3,1],[1,2],[2,2],[3,2]]

def optimalUtilization(listA, listB, target):
    # consider corner cases
    # bruteforce: m*n
    # sorting time: m*lgn+n*logn (m+n) two pointer time: m+n, worst case:m*n(当listB所有item都一样时)
    # A: [1,2,3,5,7] B:[2,4,6,6,6,8] target:8
    # 这里我们先根据每个list里的element的第二个element即value来sortA和B两个lists
    listA.sort(key=lambda x:x[1])
    listB.sort(key=lambda x:x[1])
    # 这里我们使用一个两头two pointer的方法 思想如下
    # 假设我们的A和B两个list就时第14行的两个list
    # 那么bIndex从B的最右端即8开始，aInde则从A的最左端即1开始
    # 很明显1+8=9>8 这时我们要把indexB向左移动让它指向一个更小的数字，一定不能把indexA向右移动
    # 那样的话indexA指的数字反而更大了，那么两个数字的和一定也更大
    # 正确移动后，bIndex指向6，aIndex指向1，6+1=7<8 合适
    # 那么此时我们就要保持indexB不变，不断向右移动indexA，直到两个index指向的数字之和大于target，
    # 当两数之和大于target时，再把indexB向左移动。
    # 这里有一个要注意的地方，即当indexB指向4时，indexA指向3。这就使得4和1以及4和2的组合从来都没有被考虑过
    # 实际上并不需要考虑它们，因为6和1已经6和2这样的组合我们都考虑过了，且我们知道他们是小于等于target的
    # 那么一个比6要小的4和1以及2的组合就没有必要考虑了，因为它们的和一定更小，而我们要找的是
    # 和小于等于且最接近于target的
    aIndex = 0
    bIndex = len(listB)-1
    closest = (-1)*float("inf")
    res = []
    while aIndex<len(listA) and bIndex>=0:
        currSum = listA[aIndex][1] + listB[bIndex][1]
        if currSum > target:
            bIndex-=1
        else:
            if currSum>=closest:
                if currSum>closest:
                    closest = currSum
                    res = []
                res.append([listA[aIndex][0],listB[bIndex][0]])
                # 这里还有一个要注意的地方，即如果listA里有重复的数字的话，不怕，因为
                # 我们会保持bIndex不动，不断向右边移动aIndex，这样同一个bIndex和所有这些A里相同的元素
                # 的组合我们都会考虑到。但是如果B里面有相同的元素的话，只靠现有的框架就不够了。对于
                # 每一个合格的A和B里的元素的组合，我们都要手动check一下当前bIndex指向的元素左边
                # 有没有和它值相等的元素，如果有那么要把这些元素和aIndex所指的元素的组合都考虑进去
                # 注意check bIndex左边的元素时，不能真的改变bIndex的值，而是要用一个tempBIndex
                tempBIndex = bIndex-1
                while tempBIndex>=0 and listB[tempBIndex][1] == listB[bIndex][1]:
                    res.append([listA[aIndex][0],listB[tempBIndex][0]])
                    tempBIndex-=1
            aIndex+=1
    return res
# listA = [[1,11],[2,11],[3,11]]
# listB = [[1,9],[2,9]]
listA = [[1,2],[2,4],[3,6]]
listB = [[1,2]]
print(optimalUtilization(listA,listB,7))


