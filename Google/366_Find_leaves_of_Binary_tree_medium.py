# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 如果这道题用蛮力方法解决的话，那需要dfs traverse一遍，把所有leaf node的value都加到res[0]这个sublist里，切断leafnode和它们parent之间的联系
# 再次traverse，把新的leafnodes加到res[1]这个sublist里。但是这样一来上面的nodes就要被traverse很多次，具体的time 应该接近于nlogn
# 如何optimize呢？答案是要利用resursive traveral的bottom up的特点，即当一个node在recursive call中发现自己是一个leaf node以后要给call他的parent
# return自己的level，即return 0，那么这样parent接到了这个0以后就知道我的一个child是一个leaf node了。parent的level是通过自己的child 的level来判断的，
# 具体是level(parent)=1+max(level(parent.left),level(parent.right)).我们可以发现实际上一个node的level就是它在res中应该被append to的那个sublist在res中的index
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root,res):
            # 实际上是leafnode的child none发现自己的level是-1，之后return给leafnode，leafnode才知道自己的level是0，之后再逐级告诉自己祖先们
            if root is None:
                return -1
            level= 1+max(helper(root.left,res),helper(root.right,res))
            # 当code进行到下面一行时，len(res)一定至少是等于level了。因为能执行到这一行，说明level比当前root node底的node的recursive call都已经执行完了
            # 在执行那些低级node的recursive call时，对应它们level的sublist已经在res里被建好了
            # 如果当前node是我们遇到的第一个这个level的node，那我们给他新建一个res里属于他这个level的sublist
            if len(res)<level+1:
                res.append([root.val])
            else:
                res[level].append(root.val)
            return level
        res=[]
        helper(root,res)
        return res