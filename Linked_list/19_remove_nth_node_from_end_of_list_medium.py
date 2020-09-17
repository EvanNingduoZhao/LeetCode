# 写next尤其是next.next的时候尤其要考虑是不是整个loop中都有所指的element有没有想要access None.next的情况
#这道题用一个two pointer来解，fast和slow两个pointers都从自建的连接到head左边的dummy开始，fast先向前走n步
#之后此时fast和slow开始以同样的速度往前走，直到fast走到了linkedlist的最后一个node，在这个过程中fast和slow之间的
#距离一直保持是n。在fast是最后一个node时，slow指向的那个node的下一个node就是我们要remove的
# 因为对于dummy 1 2 3 4 5这个linkedlist而言，要remove n=3那个node的话，remove的是3，fast从3开始，slow从dummy开始
#两者一直中间隔两个node，fast到5时，slow指向2

#这里之所以要用一个dummy连在head前面是为了不让要remove head的情况变成一种特殊情况。假设对于1 2 3 4 5这个linkedlist
#我们要remove n=5那个node也就是1，但是fast从1开始的话往前走4步就到linkedlist的最后一个node了，所以加一个dummy，
#这样走5步正好到最后一个node，slow还在dummy，让dummy.next=dummy.next.next,从而去掉了head node
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #考虑edge case
        if head is None:
            return Node

        else:
            dummy=ListNode(-1)
            dummy.next=head
            fast=dummy
            slow=dummy
            counter=0
            while counter<n:
                fast=fast.next
                counter+=1
            while fast.next is not None:
                fast=fast.next
                slow=slow.next
            slow.next=slow.next.next
            #即使题目要remove的是原本的head node时，dummy.next指向的也是最后该return的head
            return dummy.next