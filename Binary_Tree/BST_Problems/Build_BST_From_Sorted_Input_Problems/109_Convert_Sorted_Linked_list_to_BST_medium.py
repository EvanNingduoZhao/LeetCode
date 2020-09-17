#这是第一种recursive的解法
#讲解link https://www.youtube.com/watch?v=H8hoDlakuK4
#这道题的recursive解法的思路和108题是一摸一样的
#在108题里我们采用了slicing array的方式来进行recursion
#实际上linked list也可以进行slicing，方式就是把你要切掉的地方的next变成None
#这样一个linked list就被slice成两个了 第一个的head还是原来的head，第二个的head是切掉的地方的下一个

#当然这里实际上我们需要把linked list切成三段，中间那个node mid自己作为一段，mid左边的所有node是一段，
#mid右面的所有node是另一段
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #edge（base） case：
        #这里只处理一段linked list里只有一个node 和一个node也没有的情况
        # 108题的code里我还单独处理了array slice里只有两个element的情况，
        # 这只是为了便于理解，实际上是不用的，因为对于有两个element或node的list或者linked list
        # 是可以正常计算mid的，会被切成  mid（第二个node），left（第一个node），right（没node）

        #没node直接return none
        if not head:
            return None
        #只有一个node，就return以这个node的val为val的treenode
        if not head.next:
            return TreeNode(head.val)

        # findMid这里是用快慢指针方法写的
        #注意是怎么利用keep track of prev来切段linked list的
        def findMid(head):
            fast = head
            slow = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None
            return slow

        mid = findMid(head)
        node = TreeNode(mid.val)
        #这里我们需要在findMid里就把linked list从Mid前面切开
        #这样得到的left slice的head虽然还是原来的head，但是这个slice到Mid前面那个node为止就结束了
        node.left = self.sortedListToBST(head)
        #right slice直接从mid后面那个node开始，直到linkedlist结尾，对于right是不用切割的
        #不需要把mid和mid.next之间切开，直接把mid next作为head开始就好了
        node.right = self.sortedListToBST(mid.next)
        return node

#以上这种方法的time complexity是 O（NlogN）具体的推导见下面link里第一种方法的complexity analysis
#简单的推导就是这个方法的time cost基本上都是源自用来找每个chunck的mid node的two pointer
#在没切时一次two pointer时n，切成两半以后每一段是n/2，一共还是n，由此类推分到每一段只有1个node时，一共分了logn次
#每次总共都是n所以一共是nlogn
# space complexity是O（logN）这个比较好理解，用recursion解决的问题，主要的space complexity就是
# 来及与recursion stack，而对于解决binary tree问题的recursion的recursion stack而言，它所占的空间
# 等于Binary tree的height，而因为题目中的BST是height balanced的，所以它的height一定等于logN

#第二种方法很好想也很好写，就不在这边具体讲了
#第二种方法是先把linked list里的所有node的value按顺序存在一个list里
#再直接用108题的方法
#这种方法相较于第一种方法是一种用空间换时间，把整个linked list存在list里需要的空间就是N加上recursion stack
#是logN，一共N+logN实际还是N
#但因为对于list而言findmid只take O（1）所以recursion部分是take 1*logN=logN，而把linked list存在list里
#take N，N+logN一共还是N

#第一种方法Time是 O（NlogN）Space是O（logN）
#第二种方法Time是 O（N）    Space是O（N）

#现在我们介绍第三种方法，是最好的，Time是O（N）Space是O（logN）
#首先我们要分析一件事，对于一个sorted的linked list或者list也好，把它们convert成一个BST
#实际上它们的每一个element或者node的val是多少不重要，在这个convert 过程中真的重要的是它有几个element
#对于每一种有特定数量的node或者element的sorted list或者linked list，它们convert出来的BST的结构都是完全一样的

#也就是说我只要知道了我面对的这个linked list有几个node，我就可以算出来convert出来的BST应该是什么结构
#有几层，哪个treenode有left child，有right child，哪个没child等等

#怎么算的？ 通过下面这种left right mid index的方式算的，这里的index不是真的去index linked list里的node
#而是只为了抓出来left大于right的tree node position，对于这样的position 我们不放node

#那么我们现在知到了我们convert出来的BST哪里放node哪里不放，现在要解决的问题就是，把这些sorted的value按
#什么order放到每一个该放treenode的position里。答案是inorder，因为inorder traversal一个BST得到的是从小
#到大sorted的values，同理用从小到大sorted的values建造BST也得按inorder traversal的顺序往每一个该放treenode
#position里放进去

class Solution:

    def findSize(self, head):
        ptr = head
        c = 0
        while ptr:
            ptr = ptr.next
            c += 1
        return c


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Get the size of the linked list first
        size = self.findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            # Invalid case
            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form
            # the left half
            # 这边在刚开始call convert这个function的时候，每次都会走到这一行就在这开始了下一级
            # 的recursion，直到mid被减得小于l了，这样left就return了none
            # 这样之后才会走到node=TreeNode（head.val）这一行，所以这时linkedlist里的一个node
            # 就变成了BST里左下角那个node，并且他的left child等于left，也就是None
            # 再下面就开始求这个node的right child该是什么了
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)
            return node
        return convert(0, size - 1)