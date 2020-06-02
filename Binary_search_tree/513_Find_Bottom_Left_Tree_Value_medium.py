#这道题问最底层的最左边的node的value
#跟level有关的问题都用BFS来traverse
#637题也是BFS和这道题一起看
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return None
        else:
            #frontier代表目前正在traverse的这个level
            #frontier是一个queue
            frontier=[root]
            #在traverse frontier的过程中，把每一个frontier里的node的child nodes都enqueue到next_level里
            next_level=[]
            #每到一个新的level的第一个node，就把它的value存到first_node_value
            #如果等下发现这个level已经是bottom level了就return这个value
            first_node_value=None
            iffirst=True
            while True:
                #traverse 目前的level
                while frontier:
                    node=frontier.pop()
                    #把每个level第一个node的value存起来
                    if iffirst:
                        first_node_value=node.val
                        iffirst=False
                    if node.left:
                        next_level.insert(0,node.left)
                    if node.right:
                        next_level.insert(0,node.right)
                #next_level里什么都没有说明目前的frontier已经是bottom level了，return first_node_value
                if len(next_level)==0:
                    return first_node_value
                #next_level不是空的话就让frontier等于next_level,并把next_level清空
                #准备好store下一个level的node的child nodes
                else:
                    frontier=next_level
                    next_level=[]
                    iffirst=True