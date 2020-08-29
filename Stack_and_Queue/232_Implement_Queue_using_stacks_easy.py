#这道题是用两个stack来实现一个queue

#下面写的是一种方法，实际上还有另一种方法，但是没有下面写的这种好

#另一种方法是让push take O(N), pop take O(1)
#即每次要push的时候，先把stack1里已经有的内容全部都转移到stack2里，这样stack1的开头就空出来了
#这时把要push的东西push到stack1的开头，之后再把转移到stack2里的东西再转移回来。
#这样一番操作以后的结果就是，新push进来的，被放到了stack1的开头，原来就在stack1里的内容还是以原来
#的顺序紧跟在新push进来的那个value后面。这样就达到了以后，每次push都push到开头，那么每次从stack1
#里pop出来的stack1末尾的那个value就一定是最先被push进stack1里的，符合queue的要求

#为什么这个方法不如我下面写的这个呢：
#我们把这个方法叫做方法2，下面写的叫方法1
#首先方法1里push一定只take O(1), 方法2里pop一定只take O(1)
#但是方法1里的pop只要pop过一次，stack2里有东西了以后，直到stack2被pop完之前，每次pop都只take O(1)
#这样根据Amortized Analysis(摊销分析)的角度，pop也只take O(1)
#关于Amortized Analysis的O(1)的推导详见
#https://leetcode.com/problems/implement-queue-using-stacks/solution/
#看这个里面Approach 2的Solution

#而方法2里除非每push一次之后就pop一次，一直保持stack1是空的，这样push才能take O(1)
#说白了 方法1里 pop一次以后，把stack1里的东西转移到stack2里，这样折腾一次可以造福以后的pop，直到
# stack2被pop光

#但是方法2里的push，每次折腾到stack2里在折腾回来并不能造福下一次的push，反而你push进去的越多，
#下次需要折腾到stack2里再折腾回来的就越多
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    #在stack2里没东西的时候，要pop的话
    #得把stack1里的东西挨个pop出来，每pop出来一个就把它push到stack2里去了
    #这样以来最先进到stack1里的value会最后一个被push到stack2里
    #因此等stack1里的被全部转移到stack2里以后，pop stack2得到的结果就是我们想要的那个
    #当时第一个进入stack1的value

    #在stack2里有东西时（因为之前已经pop过了 所以已经从stack1向stack2里转移过一次了）
    #就直接pop stack2就可以了
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2:
            return self.stack2.pop()
        else:
            v = None
            while self.stack1:
                v = self.stack1.pop()
                self.stack2.append(v)
            return self.stack2.pop()

    #在stack2里，index越靠后的是越先被push进stack1的
    #在stack1里，index越靠前的是越先被push进stack1里的
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    #得stack1和stack2两个stack里都什么都没有的时候这个queue才是empty的
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()