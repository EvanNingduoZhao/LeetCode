

class Solution:
    # my solution
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # the base case can cover the case in which both l1 and l2 are none
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        # when neither of l1 and l2 is none
        else:
            # assign the head of the new list(merged list) to be the smaller one between l1 and l2
            if l1.val <= l2.val:
                newhead = l1
                l1 = l1.next
            else:
                newhead = l2
                l2 = l2.next
            # since we have to return newhead, we cannot use it as an iterator
            # we use newcurr as our iterator
            newcurr = newhead
            # the termination condition of the while loop is one of the linked list reach its end
            while l1 and l2:
                if l1.val <= l2.val:
                    newcurr.next = l1
                    l1 = l1.next
                else:
                    newcurr.next = l2
                    l2 = l2.next
                newcurr = newcurr.next
            # then we append the rest of the other list to the end of the merged new list
            # note: linked list is different from structures like array, since now l1 or l2 is still connected
            # with all the nodes behind it. instead of include every node behind it into new merged list
            # we just have to point the next of newcurr to it.
            newcurr.next = l1 or l2
        # return the head of the new merged list
        return newhead


    # below are another two methods found in discussions
    # recursively
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # in-place, iteratively
    def mergeTwoLists3(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next