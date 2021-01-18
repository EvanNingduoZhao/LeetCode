"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 这道题最直观的解法是用一个BFS traversal，把每个layer里的node都存到一个list里，之后把每个list里的所有node
# 通过它们的next给连起来，但是这个方法需要用queue来进行bfs，之后每个layer的node还得单独存一个list
# 空间复杂度是N，我们这道题要求的空间复杂度是1
# 那怎么办呢？通过观察我们可以发现，一个layer的所有node都被next给连起来以后实际上就形成了一个linked list
# 我们在经过第N给layer时，就可以把它们的children，即属于第N+1个layer上的node用next连起来形成一个linked list
# 这样我们只要存好第N+1个layer的最左边的node在一个variable里（即N+1 layer的linked list的head）
# 那么我们就可以在第N个layer走完了以后，从N+1 layer的这个head开始沿着这个N+1 layer的linked list往前走
# 边走边把第N+2个layer的node也这样穿成一个linked list。那我看第N个layer的linked list是怎么弄好的？
# 答案是在走第N-1个layer时弄好的。

#利用这个方法我们不需要queue就可以进行BFS，而且边走就边穿好linked list，每个node的next在沿途就set好了
#也不需要把每个layer的node再存到一个单独的list里之后在把list里的node都连起来这样的操作了
#因此这个方法只需要时刻维持第N个layer的开头，第N个layer上我们目前所在的node，
#第N+1个layer的开头，第N+1个layer上我们目前所在的node，这四个variable，因此空间复杂度为1

# 下面的variable name采用的是简写，ls是layerStart，lc是layerCurrent，nls是newLayerStart，
# nlc是newLayerCurrent

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        ls=root
        ls.next=None
        lc=root
        nls=None
        nlc=None
        while True:
            # lc是第N个layer中我们目前所在的node，如果lc是None，那说明第N个layer我们走完了
            if lc==None:
                # 如果第N+1个layer的start不是空，那说明还有下一个layer，我们让lc等于下一个layer的开头
                if nls:
                    lc=nls
                    # 同时把nls和nlc设成None，准备存N+2 layer里的node
                    nls=None
                    nlc=None
                #如果第N+1 layer的start是空，那说明整个tree我们都弄完了，直接return就好了
                else:
                    return root
            # 以上是每个while loop开头的check
            # 如果nls是空，那说明我们还没找到N+1layer的开头node
            # 我们应该把第N个layer的第一个有children的node的left children设为nls
            # （如果第一个有children的node没有left child那就社right child为nls）
            if not nls:
                if lc.left:
                    nls=lc.left
                    # 每次设定了nls以后 我们让nlc等于nls
                    # 之后nls是不动的，一直指向N+1 layer的开头node，等待第N个layer走完以后
                    # 我们让lc指向nls。在我们走过第N个layer的过程中，是nlc不断向前运动
                    # 慢慢用第N个layer的node的children来编织第N+1layer的linked list
                    nlc=lc.left
                if lc.right:
                    # 如果走到当前lc的right时，nls还是空（因为前面走过的lc没有children，且目前的lc只有right child）
                    # 那么当前lc的right child就是N+1 layer的第一个node，设nls等于lc.right
                    if not nls:
                        nls=lc.right
                        nlc=lc.right
                    # 如果此时nls已经不是空了，那么说明nls已经被设成当前lc的left child了，那么我们只要移动nlc就好
                    # 开始慢慢编织N+1 layer的linked list
                    else:
                        nlc.next=lc.right
                        nlc=nlc.next
            #如果nls已经不是空，那么我们就逐次移动nlc，编织N+1 layer的linked list
            else:
                if lc.left:
                    nlc.next=lc.left
                    nlc=nlc.next
                if lc.right:
                    nlc.next=lc.right
                    nlc=nlc.next
            # 每次while loop iteration的结尾，我们向前移动lc
            # 之后下一次while loop iteration的开头，我们check新的lc是不是none
            lc=lc.next