#这道题问的其实就是Trie learning notes里的内容
#处了startsWith这个function以外
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # Note:root is not a char, 它的每一个child才是各个prefix或者word的开头char
        # 即root是一个* *的children们才开始是字母
        curr = self.root
        for char in word:
            index = self.charToIndex(char)
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for char in word:
            index = self.charToIndex(char)
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            index = self.charToIndex(char)
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        # StartsWith和Search唯一的区别就是pass进来的prefix的结尾char对应的node的isEndOfWord不需要是True
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)