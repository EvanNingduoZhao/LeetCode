
def isPalindrome(head):
    # first determine two base cases
    if head is None:
        return True
    elif head.next is None:
        return True
    # push everything after the mid point into a stack, then pop values out of the stack and compare
    # them to the first half of the linked list
    else:
        s = []
        # since we will count the midpoint twice so we let length to start at 0 (this means not counting the first node)
        length = 0
        # use a two pointer technique to find the mid point
        # since we don't need the first half of the linked list to be in the stack
        # so we only start push node values into the stack at the mid point
        # when the linked list has odd number of nodes, slow end up to be the mid point
        # when the linked list has even number of nodes, slow end up to be the first node of the second half
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # push all node values starting at the mid point into a stack
        while slow:
            s.append(slow.val)
            length+=1
            slow = slow.next
        popCount = 0
        current = head
        # compare the popped values from the stack with the first half of the linked list
        while True:
            pop = s.pop()
            # if two value aren't equal, linked list is not palindrome
            if current.val != pop:
                return False
            popCount+=1
            current = current.next
            # when linked list has even number of elements then when 2*popCount = length means we have
            # already examined enough nodes to say its a palindrome
            # when linked list has  odd number of elements then when 2*popCount+1 = length means we have
            # already examined enough nodes to say its a palindrome
            if 2*popCount == length or 2*popCount+1 == length:
                return True


# my method above is using stack, below is an inplace method found in discussion
def isPalindrome(head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True
