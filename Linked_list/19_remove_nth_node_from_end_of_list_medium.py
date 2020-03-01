# 写next尤其是next.next的时候尤其要考虑是不是整个loop中都有所指的element有没有想要access None.next的情况
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return head
        # if the linked list is only consisted of one node, then head.next is none so trying to
        # access head.next.next would result in error
        # when list length is 1, then n can be either 0 or 1,  直接分类讨论这两种情况
        elif head.next is None:
            if n==0:
                return head
            else:
                return None
        # here is a two pointer technique, we first move fast n steps ahead
        # then we start to move slow and head at the same pace
        # then when fast reach the end of the linked list
        # slow.next is the node we want to remove
        else:
            slow = head
            fast = head
            counter =1
            while counter<=n:
                if fast.next:
                    fast = fast.next
                    counter+=1
                #in this case n equal the length of the linked list so we just remove the head
                else:
                    return head.next
            while fast.next:
                fast =fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head