# This problem is a basic skill question, you know or you don't know, doesn't involve asking you
# to come up with an innovative algorithm, remember this

# there are two ways to reverse a linked list, a iterative method and a recursive method, remember both
# here is a link to a good tutorial video
# https://www.youtube.com/watch?v=O0By4Zq0OFc
# also made detailed notes on Ipad under leetcode section

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Linkedlist constructor has no parameters, since we will use the insert method to put head node
        # in. So we always set head to be None when initializing an Linkedlist instance.
        self.head = None

    # traverse the entire linked list to find its length
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length +=1
            currentNode = currentNode.next
        return length

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def insertHead(self,newNode):
        temporaryNode = self.head
        self.head = newNode
        self.head.next = temporaryNode
        del temporaryNode

    # position is the position of the node (node B) in the current linked list that will be after the newNode after
    # it got inserted
    def insertAt(self, newNode, position):
        # make sure the position entered is valid
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        # position == 0 is a special case since at this point we don't have previousNode
        # so we can just use the insertHead method that we already have
        if position == 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            # we have to get access to node B and point the next of the new node to it
            # but when we are actually at node B, there's no way to go back to node A (the one should
            # be before the new node after it got inserted) so we have to save node A in previousNode
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition+=1

    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                # notice we want to stop at the last node, if we go into the next of the last node
                # which is None, then there is no way back
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next =  newNode

    def deleteHead(self):
        if self.isListEmpty() is False:
            previousHead = self.head
            self.head = self.head.next
            previousHead.next = None
        else:
            print('Linked list is empty, Delete failed')

    def deleteAt(self, position):
        if position < 0 or position >= self.listLength():
            print('Invalid Position')
            return
        if position == 0:
            self.deleteEnd()
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = currentNode.next
                currentNode.next = None
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

    def deleteEnd(self):
        # to accomplish the task of deleting the last node in a linked list:
        # we have to accomplish two things:
        # 1. find the last node
        # 2. set the next of the second to the last node as None
        # Therefore, in order to not lose access to the second to the last node after we reach
        # the last node, we keep track of a previousNode variable
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None

    def printList(self):
        if self.head is None:
            print("List is empty")
        currentNode = self.head
        while True:
            # notice if we write currentNode.next is None, then we will not be able to print the last node
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

    def reverseList_iterative(self,head):
        prev = None
        curr = head
        nex = None
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

    def reverseList_recursive(self,head):
        if head is None or head.next is None:
            return head
        reversedhead = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return reversedhead


# build a test case [1,2,3,4,5]
firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)
forthNode = Node(4)
fifthNode = Node(5)
linkedList1 = LinkedList()
linkedList1.insertEnd(firstNode)
linkedList1.insertEnd(secondNode)
linkedList1.insertEnd(thirdNode)
linkedList1.insertEnd(forthNode)
linkedList1.insertEnd(fifthNode)
#linkedList1.printList()


# this returns a node, but while executing this line, the order of linkedList1 is reversed
# the original head with value 1 now doesn't have a next so when we print linkedList 1 later
# it only gives us 1
# just understand the two lines below, don't de-comment them since if they are executed first then when later running line 175的时候
# linkedList1就已经不是原来的linkedList1了

# linkedList1.reverseList_recursive(linkedList1.head)
# linkedList1.printList()

# to see the full content of the reversed linked list, we have to insert the returned head node as head into a new linked list ans
ans = linkedList1.reverseList_recursive(linkedList1.head)
ansList = LinkedList()
ansList.insertEnd(ans)
ansList.printList()
