class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    # These are the recursive implementation of the three ways to traverse a binary tree
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """node itself -> left subtree ->right subtree"""
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """ left subtree -> node itself -> right subtree"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right,traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """ left subtree -> node itself -> right subtree"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal

# Now we start working with binary search trees, they are a special kind of binary trees
# where left child of a node is smaller than node itself and right child is bigger than node itself
class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # if the root of a BST is none then we let the node to be inserted to be its root
        if self.root is None:
            self.root = Node(data)
        # else we use a helper function defined below to perform the dirty work of comparing
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
         if data < cur_node.value:
             # if data is smaller than the value of the current node and current node has no left child
             # it means that data should just be inserted as the left child of the current node
             if cur_node.left is None:
                 cur_node.left = Node(data)
             # if the current node has a left child then we call the _insert function recursively
             # with the left child of the current node as the second parameter
             else:
                 self._insert(data,cur_node.left)
         elif data > cur_node.value:
             if cur_node.right is None:
                 cur_node.right = Node(data)
             else:
                 self._insert(data, cur_node.right)
         # BST does not allow duplicate entries
         else:
             print("value already present in tree ")

    def find(self,data):
        if self.root:
            # again use _find helper function to do the dirty work
            is_found = self._find(data,self.root)
            return is_found

    def _find(self, data, cur_node):
        # if data is smaller or greater than the value of the current node
        # but the current node does not has a corresponding left or right child
        # then it means that the BST does not contained the searched value (covered by else)
        if data > cur_node.value and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.value and cur_node.left:
            return self._find(data, cur_node.left)
        elif data == cur_node.value:
            return True
        else:
            return False

    def height(self, node):
        # this is the base case
        # since we define the leaf nodes to be of height 0
        # and we will add 1 to the max of left height and right height
        # so we return -1 here
        if node is None:
            return -1
        # the height of a particular node is the max height of it left subtree and right subtree plus 1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1+max(left_height, right_height)

    # this recursive impletation use the same idea as the height function
    # the size of a tree equals to the size of it left subtree + size of its right subtree + 1
    def size_recursive(self,node):
        if node is None:
            return 0
        return 1+ self.size_recursive(node.left)+self.size_recursive(node.right)

    def size_iterative(self):
        if self.root is None:
            return 0
        stack = [self.root]
        size = 1
        # this is very similar to the iterative implementation of the three order traversal
        while stack:
            node = stack.pop()
            if node.left:
                size+=1
                stack.append(node.left)
            if node.right:
                size+=1
                stack.append(node.right)
        return size

    def is_bst_satified(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root,self.root.value)
            # since the helper method below only returns false when violation found
            # is the binary tree satisfy the properties of BST
            # the variable is_satisfied will be None, since the helper function returned nothing
            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, cur_node, data):
        # check if the children of every node satisfy the BST property
        # return false if violation found
        if cur_node.left:
            if data > cur_node.left.value:
                return self._is_bst_satisfied(cur_node.left,cur_node.left.value)
            return False
        if cur_node.right:
            if data < cur_node.right.value:
                return self._is_bst_satisfied(cur_node.right,cur_node.right.value)
            return False



#           1
#          / \
#         2  3
#        /\ / \
#       4 5 6 7
#              \
#              8

# set up the tree as above
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(11))
print("the height if bst is ", bst.height(bst.root))
print("the size of bst is ", bst.size_recursive(bst.root))
print("is bst a satisfied BST? ",bst.is_bst_satified() )