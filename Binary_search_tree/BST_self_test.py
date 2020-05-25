class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__ (self,root):
        self.root=Node(root)


    def print_tree(self,traversal_type):
        if self.root:
           if traversal_type == "preorder":
               return self.preorder_print(self.root,"")
           elif traversal_type == "inorder":
               return self.inorder_print(self.root, "")
           elif traversal_type == "postorder":
               return self.postorder_print(self.root, "")
           else:
               print("The traversal type "+ traversal_type + " is not supported.")
        else:
            print("Binary tree is empty")

    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value)+'-')
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    def postorder_print(self,start,traversal):
        if start:
            traversal = self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal

# Now we start working with binary search trees, they are a special kind of binary trees
# where left child of a node is smaller than node itself and right child is bigger than node itself
class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,cur_node,data):
        if data< cur_node.value:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self._insert(cur_node.left,data)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(cur_node.right,data)
        else:
            print(str(data)+ " is  already present in the BST")

    def find(self,data):
        if self.root:
            is_found = self._find(self.root,data)
            return is_found
        return False


    def _find(self,cur_node,data):
        if data< cur_node.value and cur_node.left:
            return self._find(cur_node.left,data)
        elif data > cur_node.value and cur_node.right:
            return self._find(cur_node.right,data)
        elif data == cur_node.value:
            return True
        else:
            return False


    def height(self,node):
        if node is None:
            return -1
        return 1+max(self.height(node.left),self.height(node.right))


    def size_recursive(self,node):
        if node is None:
            return 0
        return 1+self.size_recursive(node.left)+self.size_recursive(node.right)

    def size_iterative(self):
        if self.root is None:
            return 0
        stack = [self.root]
        size=1
        while stack:
            node=stack.pop()
            if node.left:
                size+=1
                stack.append(node.left)
            if node.right:
                size+=1
                stack.append(node.right)
        return size

    def is_bst_satified(self):
        if self.root is None:
            return True
        else:
            is_satisfied = self._is_bst_satisfied(self.root,self.root.value)
            if is_satisfied is None:
                return True
            return False

    def _is_bst_satisfied(self,cur_node,data):
        if cur_node.left:
            if data>cur_node.left.value:
                return self._is_bst_satisfied(cur_node.left,cur_node.left.value)
            return False
        if cur_node.right:
            if data<cur_node.right.value:
                return self.is_bst_satified(cur_node.right,cur_node.right.value)
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
