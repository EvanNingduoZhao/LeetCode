# 这道题要求实现一个insert delete和getRandom都是O（1）的data structure
# 光用一个hashset是不行的，因为虽然hashset的insert和delete可以做到O(1)，但是由于
# hashset不能被access by index所以getRandom用hashset没法做到O（1）
# 改进的办法使用一个dict和list的组合，dict的key是insert进去的val，value则是这个insert进去的
# val在list里的index。每次要delete时，先用dict得到要delete的value在list中的index，知道以后
# 把list的最后一个element存到那个index处，之后把list的最后一个element pop掉，之后更新list
# 的最后一个element的值在dict里对应的key，即让dict[last_element]= index
# 最后还要在dict里用del把被delete的val对应的key value pair删掉
# 之后在getRandom时，生成一个对应着list index的random number，之后return list中那个index对应的element
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hashmap:
            index = len(self.list)
            self.hashmap[val] = index
            self.list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashmap:
            index = self.hashmap[val]
            original_last_ele = self.list[-1]
            self.list[index] = original_last_ele
            self.hashmap[original_last_ele] = index
            self.list.pop()
            del self.hashmap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        length = len(self.list)
        index = randint(0, length - 1)
        return self.list[index]
