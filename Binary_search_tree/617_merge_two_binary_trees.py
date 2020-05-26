#首先我们决定要用iterative还是recursive
#所有需要保留tree structure，return的是tree root的题都没办法用iterative
#因为把tree nodes 一个个push到stack里面以后，光用这一个stack是无法还原整个tree的结构的，因为不同结构的树
#在遍历方式一样的情况下也可能生成一样的stack

#所以这个题一看到是要return tree root就得知道要用一个recursive的方法
#因为我们这个function return的只是一个node
#那么一次recursion我们只需要解决一个node的问题
#这道题里一个node的问题就是，这个位置应不应该有一个node，有的话value应该是多少，左右child应该是什么

#实际上对于一个位置而言 无非两种情况
#1.在这个位置上两棵树都有node，那么这个位置要有node且val等于两棵树在这个位置上的nodes的values之和。并且这个
#位置的node的左右子位置也还需要用mergeTrees继续合并

#2.这个位置上只有一棵树有node或者两棵树都没node
    #1）如果只有一棵树有node的话这个位置直接把那个node放上去即可，被放上去的那个node下面还继续连着它本来就
    #连着这的左右子树，对于这个node的左右子树我们不需要合并，因为另外一棵树在这个位置上都没有node，那它在
    #这个位置的左右子位置上就更不可能有node了
    #2）两棵树这个位置都没node的话，这个位置应该放None，那自然这个位置的左右子树也不用合并了
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #第一种情况
        if t1 and t2:
            #解决这个位置要放的node的val是什么
            t1.val=t1.val+t2.val
            #解决这个位置要放的node的left child是什么
            t1.left=self.mergeTrees(t1.left,t2.left)
            # 解决这个位置要放的node的right child是什么
            t1.right=self.mergeTrees(t1.right,t2.right)
            return t1
        else:
            return t1 or t2