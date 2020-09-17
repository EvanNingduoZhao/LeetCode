#这是一道大公司常考题 一定要会 重点看！！！
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


#以下这个方法很难理解
# Approach 3: Iterative Solution without Parent Pointers
# 第三种解法也是iterative的但是不用parent pointers，虽然时间和空间复杂度和第二种方法
# 		都是还在同一个数量级的，但是第三种方法空间复杂度的常数小一些，因此更快一些。这种方法的本质即
# 		在stack遍历这个binary tree的同时，用一个variable，LCA_index存着可以能是Lowest common ancestor
# 		的那个node目前在stack里的index（因为stack是FIFO所以一个node被push进stack里了以后，只要不被
# 		pop出来，它的index是不会变的）当这个LCA_index对应的node的左子树和右子树都被遍历完了且没有发
# 		碰到p或者q的话，那么它就没有价值了，把它从stack里pop出来，把LCA_index	指向stack再先进来的一个
# 		实现这个方法需要keep track of一个node的左右子树是否已经被看过的状态，一个node可能是，左右子树
# 		都没被看过，只被看过左子树，左右子树都被看过了，这三种状态。因此我们需要用一个dict来实时记录，
# 		每一个node处于这三个状态中的哪一个。在p和q这两个node都被找到的那一刻，直接return当时
# 		LCA_Index所指向的那个node

class Solution:

    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None

#答案
#recursive的写法
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
#直接到这个link里看解释吧
#这里可以总结的一个比较重要的思路就是，不管是在BT还是BST中两个node的lowest common ancestor一定
#在这两个node中间，即这两个node肯定是一个在LCA的左子树里，另一个node在LCA的右子树里

#这个recursion是bottom up的，因此越靠下的node，只要符合right left mid三个里有两个true的前提，就会被越早return
#所以我们碰到的第一个right left mid三个里有两个true的node就一定是要找的LCA

#对于极端情况，这两个node是在一条线上的话，即一个是另一个的直接一条线上的祖先，那么他俩的LCA就是辈分高的那个

#所以从上可以总结出来的是的，如果一个node是p和q的LCA的话，那么只有三种情况，
#1 p和q一个在这个node的左子树里，一个在右子树里
#2 这个node就是p或者q中的一个，另一个在这个node的左子树里
#3 这个node就是p或者q中的一个，另一个在这个node的右子树里

#那么翻译过来就是对于一个ndoe而言left right mid这三个boolean 有两个是True的话，就return这个node
 # 需要注意的是：p或者q真的被找到的时候都是被作为mid找到的
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