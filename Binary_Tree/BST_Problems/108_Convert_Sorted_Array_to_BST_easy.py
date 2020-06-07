#这个code虽然稍微复杂了一些但是比较好理解
#对于题干中给的【-10，-3，0，5，9】这个list，这个list有奇数个elements，我们直接让median index的0左root，
#0的左subtree是-3连着-10，右subtree是5连着9。但是如果list变成【-10，-3，0，5，9，10】有6个elements的话
#还是以0为root，那0的右subtree就会是这样
#       0
#      /\
#    -3  5
#    /   \
#  -10   9
#         \
#         10
# 这样的话5这个node的左子树高度是0，右子树高度是2，height 不balanced了
# 解决办法是在0的右子树中让9做这个subtree的root，5是9的左子树，10是9的右子树，这样高度就平衡了
# 我们很容易想到如下的recursive solution
# 即一个list分成三部分，中间median element，左sublist：median左边的所有element，右sublist：median右边的所有element
# median变成node后，median的left child就是sortedArrayToBST（左sublist）
# median的right child就是sortedArrayToBST（右sublist）
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Base case
        #如果pass进来的list只有2个element的话可以直接两个连一起return
        if len(nums)==2:
            root=TreeNode(nums[1])
            root.left=TreeNode(nums[0])
            return root
        #如果pass进来的list只有1个element当然直接return这一个
        elif len(nums)==1:
            return TreeNode(nums[0])
        elif len(nums)==0 or not nums:
            return None

        # recursive body
        else:
            # //的意思是商全都round down，eg： 5//2=2
            medianIndex=(len(nums)-1)//2
            root=TreeNode(nums[medianIndex])
            #note：nums[:medianIndex]这个slice里是不包括nums[medianIndex]的
            root.left=self.sortedArrayToBST(nums[:medianIndex])
            root.right=self.sortedArrayToBST(nums[medianIndex+1:])
            return root

# 这里是一个comment里据说效率更高的code
# 因为slicing list花的时间较长，而且实际上我们每次加到BST里的也只是一个node一个node的作为某个node的
# left child 或者right child加进去的，说白了我们感兴趣的其实只是每个list slice的meidan index element
# 因为每次加到BST里的都只是val等于这个element的那一个treenode
# 因此，我们只需要keep track我们要的list slice的开头和结尾对应的是原list里的哪个index，再用开头和结尾
# 的index算出来这个list slice的median index是什么就够了
# 但是这个方法在index的计算上各种加1减1 不太好code up
class Solution(object):
    def sortedArrayToBST(self, nums):
        # Time: O(n)
        # Space: O(n) in the case of skewed binary tree.
        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node
        return convert(0, len(nums) - 1)