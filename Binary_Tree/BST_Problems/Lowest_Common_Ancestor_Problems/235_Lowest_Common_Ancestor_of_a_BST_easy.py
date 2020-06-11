#如果一个node是p q这两个node的最低公共祖先的话，那么p和q肯定是在这个node的一左一右，也就是说这个node的value
#一定是在p和q的value之间（inclusive）。
# 我们只要从root开始traverse这个BST，第一个发现的value在p和q value之间的的node就是我们要return的答案
# 为什么是inclusive呢？：因为如果在我们traverse的过程中直接就碰到了p或者q中的一个，那说明另一个是这个node
# 的后代，按照题中对于最低公共祖先的定义，我们应该直接return这个碰到的node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack=[root]
        smaller=min(p.val,q.val)
        larger=max(p.val,q.val)
        while stack:
            node=stack.pop()
            #因为我们的目的是最快找到那个value在两个node的value之间的node
            #所以碰到value比p q两个node更大的那个还大的node
            #我们就只继续看他的左子树了
            if node.val>larger:
                stack.append(node.left)
            #同理碰到比p q之间小的那个还小的，我们只继续看它的右子树
            elif node.val<smaller:
                stack.append(node.right)
            #else就是value在p q的value之间
            else:
                return node

#同样的方法，但是因为我们用stack的话其实每次也只append某个node的左或右child中的一个
#所以其实用不到stack，只需要一个curr来keep track就可以了
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        smaller=min(p.val,q.val)
        larger=max(p.val,q.val)
        while True:
            if curr.val>larger:
                curr=curr.left
            elif curr.val<smaller:
                curr=curr.right
            else:
                return curr