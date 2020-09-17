class Queue(object):
     def __init__(self):
         self.items=[]

     def enqueue(self,item):
         self.items.insert(0,item)

     # 这里我们能够用pop（）是因为我们每次enqueue的时候是从list最前面加进去的
     # 那么list最后边的也就是被pop出来的肯定是最先加进去的
     # 而我们往stack里加的时候是用的append，append是从最后面加，所以同样是pop
     # 但是stack里pop出来的是最后加进去的
     def dequeue(self):
         if not self.is_empty():
             return self.items.pop()

     def is_empty(self):
         return len(self.items)==0

     def peek(self):
         if not self.is_empty():
             return self.items[-1].value

     def _len_(self):
         return self.size()

     def size(self):
         return len(self.items)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    # These are the recursive implementation of the three ways to traverse a binary tree
    # The return value of this function is a string and user need to explicitly use print() to print it out
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        elif traversal_type == "BFS":
            return self.BFS_print(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    # A few things to notice:
    # 1. why we also take start as an input parameter? if start only refers to the root node of the Binary Tree
    #    that we would like to print, then use start as an additional parameter would be meaningless since
    #    we already got self, and the root node can be accessed by self.root. However, here we are building a
    #    recursive function, the start parameter will also be used to refer to the root node of the numerous
    #    sub-trees that we need to encounter during the execution process. Therefore, in order to be able to
    #    call the function itself with the left or right child of the current root as the root of the subtrees.
    #    we have to include start as a parameter
    # 2. traversal is a string. Since we don't know the size of the BST, it would be inappropriate to use a
    #    fixed size data structure like list. Also since traversal is a string that need to be gradually built
    #    up as we go through the recursive process. basically, each recursive call need to be able to take the
    #    current state of traversal as an input, then potentially perform some modifications to it, and then
    #    return the (modified) traversal back to its caller. Therefore, traversal also needs to be included as a
    #    parameter
    # 3. preoder_print, inorder_print and postorder_print are actually helper functions for the print_tree function
    #    we use them as helpers was not just because it structurely more clear to have helper functions. In fact,
    #    it would be impossible to write print_tree without helper functions. The reason is: for print_tree the
    #    the root is fixed, its just the root of the binary tree we want to print. So we can't have a "start"
    #    parameter for print_tree. However, as mentioned above, each of the helper functions does need a "start"
    #    parameter since the root node (of subtress) for each recursive call is different. Therefore, we need
    #    to have print_tree with only the root of the whole binary tree and to say:"ok, our objective is to
    #    print the whole binary tree" and the three helper functions to do the dirty work, making the recursive
    #    calls
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
        """ left subtree -> right subtree -> node itself """
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right,traversal)
            traversal += (str(start.value) + '-')
        return traversal

    def BFS_print(self,start):
        if start is None:
            return
        # 如果没有Queue class直接写的话，可以写
        # queue=[]
        # queue.insert(0,start)
        queue=Queue()
        queue.enqueue(start)

        traversal = ''
        while queue.is_empty() is False:
            traversal+= str(queue.peek()) + '-'
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
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

    # this recursive implementation uses the same idea as the height function
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
            # if the binary tree satisfy the properties of BST
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
print(tree.print_tree('BFS'))

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
