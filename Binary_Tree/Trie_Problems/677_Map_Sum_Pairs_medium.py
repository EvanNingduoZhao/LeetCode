#这道题首先要要搞清楚一个小问题
#对于 apple 和pple这两个单词来说，在Trie里它们不是重合的，而是root有分别的两个children a和p
#a再陆续有pple四个后代，p陆续有ple三个后代

#而apple 和applee当然在apple的部分都是重合的，这是Trie存在的意义

#所以basically，对于trie里存的单词，两个开头一样结尾不一样的单词在开头是重合的，对于两个开头不一样，结尾一样
#的单词，两者没有重合的部分。因此不会出现一个node需要有两个vals的情况
# （比如e不会有两个val 一个是apple的另一个是pple的）实际情况应该是apple和pple连着的是两个不同的e node

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        self.val = None


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def charToIndex(self, char):
        return ord(char) - ord('a')
    #这里包括往上都和trie learning notes里一样的
    #只不过对于每一个isEndOfWord的node 我们都要把insert这个function的另一个parameter val存进去
    #这样以来只有每个word结尾那个字母对应的node才有val这个attribute 其他node的val都是None
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            index = self.charToIndex(char)
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True
        curr.val = val
    #这个function是trie learning notes里没有的
    def sum(self, prefix: str) -> int:
        #这个是我们要return的
        res = 0
        curr = self.root
        #先traverse到prefix的结尾对应的那个node
        #也只有在开头包含了整个prefix的word的value才能加到res里
        #所以只有prefix的结尾字母对应的node的后代的val才能加到res里
        for char in prefix:
            index = self.charToIndex(char)
            #在traverse的过程中，如果有一个prefix的字母是在Trie里没有的
            #那说明这个Trie里没有包含整个prefix的word，直接return res，which is 0
            if not curr.children[index]:
                return res
            curr = curr.children[index]
        #如果prefix本身在Tire里就是一个完整的word的话，这个word的value也要加在res上
        if curr.val:
            res += curr.val
        #用stack来iterative的traverse，prefix最后一个字母对应的node的所有后代
        stack = [curr]
        while stack:
            node = stack.pop()
            for child in node.children:
                #找出不是Nond的children
                if child:
                    #如果是EndOfWord，也就是有value，就加到res上
                    if child.val:
                        res += child.val
                    stack.append(child)
        return res