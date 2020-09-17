
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
    #上面的while loop结束后，slow指向none，node指向原本linkedlist的最后一个node
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

#这是第三种解法，纯用recursion
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # fronterPointer在整个过程中从头到尾向后走
        self.frontPointer = head

        def _recursiveCheck(current_node):
            if current_node:
                #_recursiveCheck这个method进来一上来就是又一个recursive call
                #所以直到current_node通过不断等于自己的next指向了None的时候，我们才会走过这if
                #开始执行下一个if
                if not _recursiveCheck(current_node.next):
                    return False
                #在第一次走到这个if时，current_node指向list的最后一个node，frontPointer没动过还是指向第一个node
                #从此一个从尾到头，一个从头到尾，two pointer判定palindrome的过程开始了
                if self.frontPointer.val != current_node.val:
                    return False
                #每次如果上面的if过了，就把frontPointer往前走一步，正好进入到stack的下一个recursive call时
                # current_node也相当于是往回走了一步，两者永远是指向对称的node的
                self.frontPointer = self.frontPointer.next
            #这个return True有两个作用，第一是在current_node is None时return True
            #第二是整个流程都走完了以后，如果没有碰到return False，就最后return true
            return True

        return _recursiveCheck(head)
