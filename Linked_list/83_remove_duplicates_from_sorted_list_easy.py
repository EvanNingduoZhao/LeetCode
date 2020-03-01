class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        else:
            current = head
            # we can stop immediately after we reach the last node
            while current.next:
                if current.val == current.next.val:
                    if current.next.next:
                        current.next= current.next.next
                    # in case like 1->1->2->3->3
                    # 我们在倒数第二个node的时候，后面只有一个node了，没有next.next了
                    # 所以我们直接set current.next = None
                    else:
                        current.next = None
                else:
                    current = current.next
            rturn head