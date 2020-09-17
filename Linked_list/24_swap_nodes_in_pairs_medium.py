
# 第一种recursive的method
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        #如果没有head，或者只剩下一个node了的话，就不需要swap了
        if head is None or head.next is None:
            return head
        else:
            secondNode = head.next
            #先用recursive call把目前这一对node后面的所有node都成对swap了
            #再让这一对的第一个node的next链接上后面的所有node 成对swap后的结果
            head.next = self.swapPairs(secondNode.next)
            # 最后在让这一对原本的第二个node的next链接到这一对原本的第一个node上
            secondNode.next = head
            # 完成这一组两个node的swap，return现在应该作为这一组中第一个node的secondNode
            # 这个node会作为本次recursive call的结果被return给前一次recursive call
            # 被链接到前一次recursive call中的head的next上
            return secondNode

#第二种iterative的解法
#这道题用iterative的解法要注意一个细节，假设现在有linked list A B C D，那么我们在把A和B换位置以后，变成B A
#那么A的next实际上不应该是C而应该是等C和D换了位置以后的D，但是为了简化这个问题，不考虑那么多
#我们在调换A B时先不考虑C和D的问题，直接让A的next先等于C，但是我们把A存到prevNode这个variable里
#等开始调换C和D时，在让prevNode.next=D
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #对于从第二对node开始以后的node，它们都是有它们前面的node作为prevNode的
        #那对于第一对node而言prevNode该怎么办呢？ 答案是自己造一个
        # 让自己造的dummy这个node的next是head，再让prevNode=dummy
        # 那么实际上现在prevNode和dummy就是一个node了，prevNode的next被改变时，dummy的也会被改变
        # 那么实际上dummy起到了两个作用：第一是作为第一队node的prevNode，第二记录了被swap之后的linked list
        # 的new head,即dummy.next 这也是我们最后要return的
        dummy=ListNode(-1)
        dummy.next=head
        prevNode=dummy
        while head and head.next:
            firstNode=head
            secondNode=head.next
            prevNode.next=secondNode
            firstNode.next=secondNode.next
            secondNode.next=firstNode
            #进行完上面的一系列操作后，把prevNode和head都往前移一个
            prevNode=firstNode
            head=firstNode.next
        return dummy.next
