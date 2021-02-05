# 这道题用到backtracking，这个code的写法其实和recursive traverse一个binary tree很像
# 我把recursive traverse一个binary tree粘贴到下面
# 对于这个code是怎么回事先看下面的那一大段
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits)==0:
            return None
        dic={2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']}
        res=[]
        def backTrack(combo,nextDigits):
            # 如果nextDigits是空了，说明我们刚才已经碰到了一个leaf node了
            # 那么combo，即从root到一个leaf node的path已经建立完整了
            # 可以加到res里了
            if len(nextDigits)==0:
                res.append(combo)
            else:
                # 如果nextDigits不是空，那么就还没到头
                # 我们就要把下一个digit可以对应的每一个字母都加到目前combo的尾巴上一下
                for letter in dic[int(nextDigits[0])]:
                    backTrack(combo+letter,nextDigits[1:])
        # 最开始combo是空，nextDigits就是整个input digits
        backTrack("",digits)
        return res

# 这里来将以下上面那道题和下面recursive traverse一个binary tree的共同之处
# 在recursive traverse一个binary tree里我们是想要把所有node的val都放到一个string里
# 上面的电话号码问题其实可以类比成一个tree，父子关系是由digits这个input决定的
# 一个数字a如果在digits中紧贴在一个数字b后面，那么在这个tree中每一个数字b对应的字母，都有
# 数字a对应的那一组字母作为它的child nodes。比如说对于23，那么2对应的abc，每一个字母都有
# 3对应的def这三个字母作为孩子。
# 上面的题目里我们是想找到所有的电话号码组合，所以我们不是要把这个tree中的所有node的val都放到一个
# string里。而是要找到每一条从root通往一个leaf node的path
# 在上面的code中combo就相当于下面的traversal，
# 因为在这道题中每个数字对应的字母不是真的有一个tree把它们连在一起，所以没法直接用left right child
# 这样的手段来直接access children，因此我们要用nextDigits来存着目前所在node的后代们都是什么
# 而nextDigits[0]实际上相当于下面的start
def preorder_print(self,start,traversal):
    if start:
        traversal += (str(start.value)+'-')
        traversal = self.preorder_print(start.left,traversal)
        traversal = self.preorder_print(start.right, traversal)
    return traversal