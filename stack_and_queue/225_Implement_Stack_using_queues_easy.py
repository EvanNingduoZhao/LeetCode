#以下是自己写的用两个queue的方法，这里queue采用的是左进右出的形式
#注意因为queue是FIFO，所以把values从queue1 pop出来再push进queue2，这样的转移结束后
#queue2里的value的顺序是跟原来在queue1里一样的
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.insert(0, x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #最后被push进queue 1的在queue1的最左边
        #因此我们从queue1的最右边开始pop
        #每pop出来一个就push进queue2的最左边
        #直到queue1里只剩下最后push进来的那一个value
        #我们pop那一个value就达到目的了
        #Note：就算queue2里原本就有东西，也还是要把queue1里的按顺序转移到queue2里
        if self.queue1:
            for _ in range(0, len(self.queue1) - 1):
                self.queue2.insert(0, self.queue1.pop())
            return self.queue1.pop()
        #如果queue1里没东西的话，那就反向把queue2里的转移回queue1
        else:
            for _ in range(0, len(self.queue2) - 1):
                self.queue1.insert(0, self.queue2.pop())
            return self.queue2.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue1:
            return self.queue1[0]
        else:
            return self.queue2[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1 and not self.queue2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()



# 只用一个queue的方法
# initialize your data structure here.
# 这里implement queue和上面自己写的solution的方法不一样
# 这里是右面进左面出，自己写的是左面进右面出的queue
def __init__(self):
    self.queue = collections.deque()
    self.size = 0


# 每次往右面push一个进去以后，就从左面依次pop出来一个value，把pop出来的再push进右边
# 直到新push进来的那个变成了最左边的为止，这样这个模拟stack需要pop的时候，直接pop左边第一个就好了
# @param x, an integer
# @return nothing
def push(self, x):
    self.queue.append(x)
    #这里还没increment size呢，这里self.size等于push这个新value进来之前的values的数量
    for _ in range(self.size):
        self.queue.append(self.queue.popleft())
    self.size += 1

def pop(self):
    self.size -= 1
    return self.queue.popleft()


# @return an integer
def top(self):
    # queue peek operation
    return self.queue[0]

# @return an boolean
def empty(self):
    return self.size == 0