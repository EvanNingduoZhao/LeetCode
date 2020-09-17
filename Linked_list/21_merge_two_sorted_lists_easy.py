

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

    #Leetcode官方答案，是上面自己写的答案的改进版
    #这个方法之所以好是因为：
    # 1. 首先上面自己的方法为了判断merge后的head是谁要单独用一个if else来判断谁是newhead
    #但是在答案里的方法我们采用的是先create一个newNode叫prehead的形式，之后直接开始while loop，擂台赛
    #一个一个往prehead后面链接新的node，最后把prehead.next作为merge之后的list的head return
    # 2. 其次我们不需要在一个list A全都走完了以后，特意把没走完的那个list B的剩下的部分
    # 链接到merged list后面，因为实际上把目前traverse B的那个iterator所指的那个node C链接到merged list后面就够了
    # 因为node C实际上后面还连着list B后面剩下的所有node呢
    class Solution:
        def mergeTwoLists(self, l1, l2):
            # maintain an unchanging reference to node ahead of the return node.
            prehead = ListNode(-1)

            prev = prehead
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next

            # exactly one of l1 and l2 can be non-null at this point, so connect
            # the non-null list to the end of the merged list.
            prev.next = l1 if l1 is not None else l2

            return prehead.next


    # below are another two methods found in discussions
    # recursively
    def mergeTwoLists2(self, l1, l2):
        #base case
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # in-place, iteratively
    # 为什么叫in place，因为这种方法相当于一直在l1里traverse，之后把l2里的node insert到l1里合适的位置
    def mergeTwoLists3(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        #这里让dummy 和cur在开始时，代指同一个node
        dummy = cur = ListNode(0)
        #这里实际上将cur的next也设定成了l1
        #dummy从此就不会在变化了，但是随着后面的cur=cur.next被执行之后，dummy和cur就不再是同一个node了
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                #看完后面可知，每次把一个l2的node A作为cur.next链接到l1上以后，我们都会把被A
                # 和它在l2里后面的node的链接断开，并且把A的next设置为在A被放进来之前cur后面的那个l1里的node

                #这里把cur后面的那个l1里的node存到nxt里
                nxt = cur.next
                #把node A作为cur.next连接到l1上
                cur.next = l2
                #把node A本身在l2里后面的那个node存到tmp里
                tmp = l2.next
                #让已经被链接到l1里的A的next成为A被放进来之前cur后面的那个l1里的node
                l2.next = nxt
                #让l2这个iterator指向A本身在l2里后面的那个node
                l2 = tmp
            cur = cur.next
        #这里之所以要加这一行是因为：如果l1先走完的话，其实不需要这一行，因为cur本身就是在l1里的一个iterator
        #这一行的作用是当l2先走完时，让cur的next直接连上l2里剩下的部分。因为我们不知道谁会先走完，所以要用or
        cur.next = l1 or l2
        #这里dummy的运用和leetcode官方答案里prehead的运用是一致的
        return dummy.next