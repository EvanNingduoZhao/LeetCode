# inorder 是left node-itself right
# 那么我们return的结果里的第一个应该的这个tree的最下层的最左面的那个
# 用iterative的方法去遍历BST最重要的思想就是，当stack空了的时候就说明BST遍历完了 该return了


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        #这里有一个思想：
        #preorder和postorder的iterative的遍历都是直接用while stack的，为什么这里要用while true呢
        #因为preorder和postorder都是res里面放进去一个新的node以后，不用管别的，直接吧这个node的left和
        #right child都push到stack里。这样stack在一次while loop结束以后如果是是empty的或者里面只有None的话
        #那么就可以断定我们已经遍历完这个BST了
        #但是对于inorder遍历而言每一个while loop结束后的那个root（node.right）都可能有左子树，但是这个左子树
        #是从来都没有被push进stack过的，所以要用while true，之后在这个大while loop的最开始用一个小while loop
        #来穷尽这个root（node.right）的左子树，把他们都push到stack里去
        while True:
            #先左边
            while root:
                stack.append(root)
                root = root.left
            # 在遍历BST的整个过程中只要stack有一刻为空了，那就说明这个BST遍历完了
            if not stack:
                return res
            #node自己
            #这里有一个思想，可以理解为虽然每个node都可能是其他node的left child 或者right child，但每个node一定都是
            #自己的node itself
            # 在往stack里push的时候也是要按照左 node-itself 右的顺序加到stack里，但是从stack里pop出来再加到res里的时候，
            #可以理解成这时候pop出来的都是node itself，加入到res里面以后我们就立刻开始看这个node itself的right child了
            node = stack.pop()
            res.append(node.val)
            #在看这个node的right child，有可能这个node的right child是None
            #但即将开始的while loop的下一个iteration的开头 如果现在的root是none的话就不会执行内层while 直接pop stack
            #里的下一个
            #node.right不能直接加到res里面去，因为有可能这个node.right是有left child的，所以在外层while loop的
            #最开始要先用小while loop将以node.right为root的这个sub tree的left child穷尽到底
            root = node.right
        return res