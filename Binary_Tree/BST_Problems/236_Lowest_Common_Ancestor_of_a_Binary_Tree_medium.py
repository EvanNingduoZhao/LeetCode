class Solution:
    # 自己写的，思想和下面答案的iterative using parent pointers是基本一样的
    # 看一下答案的解释就能理解自己当时写这个code的想法了
    # 自己这个和答案相比有一个缺点
    # 在dict里面每一个见过的node作为key，value不需要是这个node的所有祖先，只需要是这个node的爸爸就够了
    # 这样节省很多memeory

    #而且实际上不用纠结是先找到的q还是先找到的p
    #两个都找到以后，先随便顺着其中一个，假设是p，往前回溯，把它自己和它的所有祖先都存在一个list里
    #在沿着另一个，假设是q，回溯，找到的第一个也在p的祖先的list里的node就return
    #这个方法也cover了p就直接是q的祖先的特殊情况
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [(root, [])]
        ances_dict = {root: []}
        foundOne = False
        while queue:
            node, ances = queue.pop()
            ances.append(node)
            if node.val == p.val or node.val == q.val:
                if foundOne == False:
                    foundOne = True
                else:
                    if node.val == q.val:
                        if p in ances:
                            return p
                        else:
                            for an in ances_dict[p][::-1]:
                                if an in ances:
                                    return an
                    else:
                        if q in ances:
                            return q
                        else:
                            for an in ances_dict[q][::-1]:
                                if an in ances:
                                    return an

            if node.left:
                queue.insert(0, (node.left, ances[:]))
                ances_dict[node.left] = ances[:]

            if node.right:
                queue.insert(0, (node.right, ances[:]))
                ances_dict[node.right] = ances[:]


#答案
# Approach 2: Iterative using parent pointers
#
# Intuition
#
# If we have parent pointers for each node we can traverse back from p and q to get their
# ancestors. The first common node we get during this traversal would be the LCA node.
# We can save the parent pointers in a dictionary as we traverse the tree.
#
# Algorithm
#
# Start from the root node and traverse the tree.
# Until we find p and q both, keep storing the parent pointers in a dictionary.
# Once we have found both p and q, we get all the ancestors for p using the parent dictionary
# and add to a set called ancestors.
# Similarly, we traverse through ancestors for node q. If the ancestor is present in the
# ancestors set for p, this means this is the first ancestor common between p and q
# (while traversing upwards) and hence this is the LCA node.

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

#答案
#recursive的写法
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
#直接到这个link里看解释吧
#这里可以总结的一个比较重要的思路就是，不管是在BT还是BST中两个node的lowest common ancestor一定
#在这两个node中间，即这两个node肯定是一个在LCA的左子树里，另一个node在LCA的右子树里

#对于极端情况，这两个node是在一条线上的话，即一个是另一个的直接一条线上的祖先，那么他俩的LCA就是辈分高的那个

#所以从上可以总结出来的是的，如果一个node是p和q的LCA的话，那么只有三种情况，
#1 p和q一个在这个node的左子树里，一个在右子树里
#2 这个node就是p或者q中的一个，另一个在这个node的左子树里
#3 这个node就是p或者q中的一个，另一个在这个node的右子树里

#那么翻译过来就是对于一个ndoe而言left right mid这三个boolean 有两个是True的话，就return这个node
class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            # p或者q真的被找到的时候都是被作为mid找到的
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans