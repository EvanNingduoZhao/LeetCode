class Solution:
    original = []
    currOrder = []

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.currOrder = nums[:]

    def reset(self) -> List[int]:
        print("currOrder is:", self.currOrder)
        print("orginal is:", self.original)
        self.currOrder = self.original[:]
        return self.currOrder

    # 下面写着的是time space都为N的solution，这里再说一下自己写的不好的solution，
    # 说一下为什么自己的不好。
    # 我的solution是每次要shuffle时，create一个currentOrder的copy叫temp，之后生成一个
    # 在0和len(temp)-1之间inclusive的random int。让currOrder[i]等于temp[random int]
    # 之后把random int这个index在temp中对应的element从
    # 
    def shuffle(self) -> List[int]:
        for i in range(len(self.currOrder)):
            randIdx = randint(i, len(self.currOrder) - 1)
            self.currOrder[i], self.currOrder[randIdx] = self.currOrder[randIdx], self.currOrder[i]
        return self.currOrder