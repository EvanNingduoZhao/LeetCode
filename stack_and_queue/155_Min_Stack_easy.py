# 这个题代表了了一种典型问题，即动态的最小值
# 即在一个element会不断有新的进来、旧的出去的data structure里
# 如果最有效地keep track of min

# 以下是自己写的，代表着方法1
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    # 在push一个新的val进入stack之前，先记录起来在把这个val push进stack之前，现在stack里的最小值
    # 是多少，再把（x,temp）这封tuple push到stack里
    # 这样pop的时候，让self.min=被pop的那个tuple的第二个element即可，which记录了
    # 把被pop的那个val push到stack里之前，这个stack的最小值是多少
    def push(self, x: int) -> None:
        temp = self.min
        self.stack.append((x, temp))
        self.min = min(x, self.min)

    def pop(self) -> None:
        pop, newMin = self.stack.pop()
        self.min = newMin

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min

#这是评论里看的第二种方法
class MinStack:
    def __init__(self):
        self.data = []
        self.min = []
        self.size = 0

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.size == 0:
            self.min.append(x)
        #如果新push进data这个stack的value比目前min这个stack里存的最小的值还小的话
        #就把这个value push到min这个stack里
        #这样当从data这个stack里pop出的value的等于目前stack里的最小值的话，
        #那么只要把min这个stack里最后进来的pop掉，min这个stack里新的最后一位就是
        #新的data这个stack里的最小值
        else:
            if x <= self.min[-1]:
                self.min.append(x)
        self.data.append(x)
        self.size += 1

    # @return nothing
    def pop(self):
        tmp = self.data.pop()
        self.size -= 1
        if tmp == self.min[-1]:
            self.min.pop()

    # @return an integer
    def top(self):
        return self.data[-1]

    # @return an integer
    def getMin(self):
        return self.min[-1]