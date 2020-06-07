#跟在list里找two sum的原理是一样的
#这里的hashtable用的是python里的set（）
#因为我们只需要存已经见过的node的value，即只存values，不需要key value pairs，set就够了不需要dict
#用stack DFS traverse BST
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        else:
            stack=[root]
            s=set()
            s.add(root.val)
            while stack:
                node=stack.pop()
                #每次新见到一个node
                if node.left:
                    # 算出它和target value k相差多少
                    complement=k-node.left.val
                    # 看相差的这个complement在不在已经见过的values里
                    # 如果在直接return true
                    if complement in s:
                        return True
                    #如果不在把这个node push 到stack里
                    #把它的value加入到已经见过的values里
                    else:
                        stack.append(node.left)
                        s.add(node.left.val)
                #右侧同理
                if node.right:
                    complement=k-node.right.val
                    if complement in s:
                        return True
                    else:
                        stack.append(node.right)
                        s.add(node.right.val)
            #BST traverse完了还没发现符合的一对nodes的话就return false
            return False