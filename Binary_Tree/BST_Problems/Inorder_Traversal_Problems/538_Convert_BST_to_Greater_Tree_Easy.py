#对于BST进行传统的inorder traversal（即左 自己 右）得到的是就是从小到大的顺序
#如果我们改进一下inorder traversal 变成 右 自己 左的话那么得到的就是从大到小的顺序
#这道题让我们给每一个node的value都加上所有比自己value大的node value之和
#那么我们只需要用这个改进版的inorder traversal进行从大到小遍历，并在遍历过程中
#keep updating一个sumSoFar，在把一个current node的value加到这个sumSoFar里之前，把current value存在temp里
#再把sumSoFar加在这个node的value上

#和230题的传统inorder traversal的code对照着看
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        rootNode=root
        stack=[]
        sumSoFar=0
        while True:
            while root:
                stack.append(root)
                #因为是modified inorder traversal所以这里先穷尽right child
                root=root.right
            if not stack:
                return rootNode
            node=stack.pop()
            temp=node.val
            node.val=node.val+sumSoFar
            sumSoFar=sumSoFar+temp
            #对应的这里之前先看完了右边，现在要再看左边了
            root=node.left