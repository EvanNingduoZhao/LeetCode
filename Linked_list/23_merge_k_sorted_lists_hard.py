#第一种方法，把lists里的第一个linked list分别和剩下的所有list挨个merge
#每一次merge take N，一共merge k-1次因此time是O(kN),space是O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # edge cases
        if not lists or len(lists) == 0:
            return None
        notAllNone = False
        for i in lists:
            if i:
                notAllNone = True
                break
        if notAllNone == False:
            return None
        if len(lists) == 1:
            return lists[0]

        def _merge_two_list(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next

        for l in lists[1:]:
            lists[0] = _merge_two_list(lists[0], l)
        return lists[0]

#还是用同样的helper function，但是我们merge的策略从第一个挨个和所有的merge变成把k个lists分成k/2组list pairs
#每组的两个merge，剩下k/2个lists分成k/4组list pairs，就这样一直下去直到最后两个lists merge成一个list
#这个方法每一轮merge要take O(N)因为一共k个lists里加起来一共有N个nodes，每一次merge都要把这N个都走一遍。
#一共要merge logk轮所以time complexity是O(Nlogk),所有操作依旧是in place的所以space complexity是O(1)
#这里我们得到的思路是，类似这样的问题即k个东西merge在一起，不要某一个挨个和其他剩下的merge，而是要想这个思路一样只merge logk轮

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # edge cases
        if not lists or len(lists) == 0:
            return None
        notAllNone = False
        for i in lists:
            if i:
                notAllNone = True
                break
        if notAllNone == False:
            return None
        if len(lists) == 1:
            return lists[0]

        def _merge_two_list(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = _merge_two_list(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]