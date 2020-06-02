#这道题要求的是每个level的平均值，自然想到BFS遍历
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return None
        else:
            #frontier里装着目前所在的level的node
            frontier=[root]
            #在遍历目前所在level的node时，把它们的children装进next_level这个list
            next_level=[]
            #res用来存每个level的average，这是最后要return的
            res=[]
            #count是每个level的node数量，最开始为1因为root这个level只有root一个node
            count=1
            #level_sum用来keep track目前这个level的sum
            level_sum=0
            while True:
                #遍历目前这个level
                while frontier:
                    node=frontier.pop()
                    level_sum+=node.val
                    if node.left:
                        next_level.insert(0,node.left)
                    if node.right:
                        next_level.insert(0,node.right)
                #一个level遍历完了算出来average，加入到res里
                res.append(level_sum/count)
                #如果一个level遍历完了以后next_level是空的，那说明整个binary tree都遍历完了
                if len(next_level)==0:
                    return res
                #next_level不是空的话就开始遍历下一个level
                # 先把level_sum归零
                # 这里的next_level存着下一个level的所有node所以让count等于next_level的len
                #  让新的frontier等于目前的next_level，再把next_level清空，准备好存下一个level的children
                else:
                    level_sum=0
                    count=len(next_level)
                    frontier=next_level
                    next_level=[]