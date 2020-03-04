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
