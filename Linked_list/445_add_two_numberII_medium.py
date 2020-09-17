#要求return的是一个linked List里面每一个node装着sum的一个digit
def addTwoNumbers(l1, l2):
    # we have to reach to the end of both linked list and add them up digit by digit backwards
    # (因为进位等原因 加法得从个位数开始加)
    # if we can modify the linked list then we can reverse the input linked lists when traversing
    # to the end of them, so we can have our way back later when performing addition
    # since here we are not allowed to modify the input linked list. we have to push the each node value
    # in to stack while traversing it so we can pop the value one by one when adding them
    s1 = []
    s2 = []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    # if one linked list is empty then return the head of the other linked list
    if not s1:
        return l2
    elif not s2:
        return l1
    else:
        carry = 0
        initialsum = s1.pop() + s2.pop()
        if initialsum > 9:
            carry = 1
            curr = ListNode(initialsum - 10)
        else:
            curr = ListNode(initialsum)

        while s1 or s2:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            sum = (x+y+carry)%10
            carry = (x+y+carry)//10
            # to insert the a new node as the head of the linked list to return
            prev = curr
            curr = ListNode(sum)
            curr.next = prev
        # it is really important to handle carry properly in the end
        if carry == 0:
            return curr
        else:
            prev = curr
            curr = ListNode(1)
            curr.next = prev
            return curr

# 可以modify list的前提下用reverse两个linkedlist做的
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #先考虑basecase
        if not l1:
            return l2
        if not l2:
            return l1
        #这是一个用recursive的方法写的用来reverselist的helper method
        def _reverseList(head):
            if head is None or head.next is None:
                return head
            reverseHead=_reverseList(head.next)
            head.next.next=head
            head.next=None
            return reverseHead
        #把两个list都reverse，之后curr1和curr2分别是两个list被reversed之后的head
        curr1=_reverseList(l1)
        curr2=_reverseList(l2)
        #算出个位数的和，确定carry是多少
        currDigit=(curr1.val+curr2.val)%10
        carry=(curr1.val+curr2.val)//10
        #给新算出来的个位数字create一个node
        currNode=ListNode(currDigit)
        prev=None
        # curr1和curr2都往前移一个
        curr1=curr1.next
        curr2=curr2.next
        #只要有一个list还每到头就继续
        while curr1 or curr2:
            #如果自己所在的list已经到头了，那么对应的value就是0
            v1=curr1.val if curr1 else 0
            v2=curr2.val if curr2 else 0
            #算出currDigit和carry
            currDigit=(carry+v1+v2)%10
            carry=(carry+v1+v2)//10
            #给新算出来的个位数字create一个node，并把新create的node连接到要return的linkedlist的最前面
            prev=currNode
            currNode=ListNode(currDigit)
            currNode.next=prev
            #如果自己所在的list还没有走完的话，pointer向前走一步
            if curr1:
                curr1=curr1.next
            if curr2:
                curr2=curr2.next
        #和上面的方法一样最后也是要注意carry是不是1的问题
        if carry==1:
            prev=currNode
            currNode=ListNode(1)
            currNode.next=prev
        return currNode
