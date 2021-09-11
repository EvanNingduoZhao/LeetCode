# 给定四个商品A,B,C,D。 然后有四个list，分别代表四个商品的不同价格。
# 比如ListA, ListB, ListC, ListD。然后给你一个budget，问你不超过这个budget，
# 每个商品买一个，一共有多少种买法。
# 比如 [1,2], [2,3],[4],[1,2,3], budget = 10
# 这道题的思路是，先把四个产品的买法组合问题，转化成两种产品的买法组合问题
# 具体的转化思路是算出所有的买A和B的买法组合要花的钱，再算出所有买C和D的买法组合要花的钱
# 把它们分别存到ABPriceCombo和CDPriceCombo里
# 把这两个list都分别sort一下
# 对于每个ABPriceCombo里的element，即买A和B两个products可能会花的钱数
# 用总的budget减去这个钱数得到：如果这样买A和B，那么还剩下多少钱可以用来买C和D
# 得到这个remaining之后，用binary search再已经sort好的CDPriceCombo里找到比remaining大的elements里最小的那个
# 那么所有在找到的这个element左边的elements（不包括找到的这个element）就都是一种valid的买C和D的方法
# 那么左边有多少个element就在res上加几

# 这个方法的time complexity是ablogab，ab是指ABPriceCombo和CDPriceCombo的平均长度，主要大头的时间是花在sort上
# 且在CDPricecombo中的每一次binary search也都话费logab，且要进行ab次这样的search，总的下来也是ablogab
def shoppingOptions(listA,listB,listC,listD, budget):
    ABPriceCombo = []
    CDPriceCombo = []
    for a in listA:
        for b in listB:
            ABPriceCombo.append(a+b)
    for c in listC:
        for d in listD:
            CDPriceCombo.append(c+d)
    ABPriceCombo.sort()
    CDPriceCombo.sort()
    print("ABPriceCombo is: ", ABPriceCombo)
    print("CDPriceCombi is: ", CDPriceCombo)
    res = 0
    for abCombo in ABPriceCombo:
        remaining = budget-abCombo
        # 这里注意假设CDPriceCombo中比remaining大的elements里最小的那个的index是5
        # 那么就说明在CDPriceCombo中index是0，1，2，3，4的这5个element是要小于等于remaining的
        # 因此在res上加5
        index = binarySearch(CDPriceCombo,remaining)
        res += index
        print("res: ", res)
    return res

# binary search function that return the index of the
# largest element that is smaller or equal to target in nums
def binarySearch(nums,target):
    print("target is: ",target)
    start = 0
    end = len(nums)-1
    while start < end:
        mid = start + (end-start)//2
        if nums[mid]<=target:
            start = mid+1
        else:
            end = mid
    print("nums[start]: ", nums[start])
    if nums[start]>target:
        return start
    else:
        return len(nums)




print(shoppingOptions([1,2], [2,3],[4],[1,2,3], 10))