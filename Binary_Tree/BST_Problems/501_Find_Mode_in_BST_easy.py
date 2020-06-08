#想一想可以得出结论，虽然这个特殊的BST允许 duplicate items
#但是inorder traversal依然可以得到从小到大的sorted node values
#所以在inorder traversal的过程中相同value的node只会连在一起出现
#我们的目标是不用extra space来解决这个问题，也就是说我们不能用dict之类的extra space来存每个node出现了几次
#也不能先inorder traversal一遍，把所有的node values都按从小到大的顺序放到一个list里


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        #我现在看到的这个node的value出现了几次
        self.count = 1
        #目前出现最多的value出现了几次
        self.maxCount = 1
        # 我们需要keep track of上一个我们见到的node
        self.prev = None
        # 要return的mode list
        self.ans = []
        self.dfs(root)
        return self.ans
    #recursive inorder traversal
    def dfs(self, root):
        if root.left:
            self.dfs(root.left)
        # 如果这是我们碰到的第一个node，我们让prev等于它
        if self.prev is None:
            self.prev = root.val
            self.count = 1
            # 这里是唯一一个能把第一个遇到的node的val放进ans的机会
            # 因为只要没有发现有一个value出现过大于等于两次，那么每见到一个新node，都要放到ans里
            self.ans.append(root.val)
        else:
            #如果目前的node的val和前一个node的val一样的话
            #说明这个value又多出现了一次
            if root.val == self.prev:
                self.count += 1
                #如果count和maxcount相等的话说明这个value出现的次数和之前出现次数最多的value的出现
                #次数一样了，所以保留之前那个出现次数最多的value的基础上，在ans里再加上这个value
                if self.count == self.maxCount:
                    self.ans.append(root.val)
                #如果目前这个value出现的次数大于了之前出现次数最多的value（们），ans里就只能又现在这个value了
                if self.count > self.maxCount:
                    self.ans = []
                    self.ans.append(root.val)
                    self.maxCount = self.count
            #如果目前node的value不等于前一个见到的node的value
            else:
                self.count = 1
                #如果现在没有value出现过大于等于两次，那么每见到一个新的value都要放到ans里
                if self.maxCount == 1:
                    self.ans.append(root.val)
                self.prev = root.val
        if root.right:
            self.dfs(root.right)