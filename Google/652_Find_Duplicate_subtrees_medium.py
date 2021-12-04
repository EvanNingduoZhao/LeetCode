# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 遇到这种比较tree或者是subtree是不是一样的问题时，一定要想到用pre order traversal来把一个subtree serilize成一个string，且null的node要用"null"来填补
# 这样我们把所有见过的string representation都存到一个dict里，发现有一个subtree的stirng是第二次见了，就把它的root append到res里
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtreeMap = {}
        res = []
        def helper(root, subtreeMap, res):
            if root is None:
                key="null"
            else:
                key = str(root.val) + ","+helper(root.left,subtreeMap,res)+","+helper(root.right,subtreeMap,res)
            # 如果key是"null",那说明root是None，两个都是None的subtree我们不算它们是duplicate subtree，所以不把None放进res
            if key!="null":
                if key in subtreeMap:
                    if subtreeMap[key]==1:
                        subtreeMap[key]+=1
                        res.append(root)
                else:
                    subtreeMap[key]=1
            return key
        helper(root,subtreeMap,res)
        return res