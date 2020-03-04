class Node:
    def __init__(self,data):
        self.data = data
        # we don't put next as a parameter since we always want next to be None when initializing and
        # Node instance
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

    # my answer
    # my code is longer since I work on 4 nodes as a group once
    def swapPairs(self, head):
        # handle the case where list length is 0 or 1
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            newhead = head.next
            head.next.next = head
            head.next = None
            return newhead
        else:
            groupStart=head
            curr = head
            # the second node should be returned as head after task completed
            head = curr.next
            # while loop terminates if no node left in the next group
            while curr:
                print('enter while loop')
                temp1 = curr
                # check if there is only one node left in the next group
                if curr.next:
                    print('if curr.next')
                    temp3 = curr.next.next
                    # check if there are only two nodes left in the next group
                    if temp3:
                        print('if temp3')
                        curr.next.next = curr
                        curr.next = temp3
                        curr = temp3
                        # check if there are only three nodes left in the next group
                        if curr.next:
                            groupStart=curr.next.next
                            print('last if')
                            curr.next.next = curr
                            temp1.next = curr.next
                            grouplast = curr
                            if groupStart:
                                if groupStart.next:
                                    curr.next = groupStart.next
                                else:
                                    curr.next = groupStart
                            else:
                                curr.next = None
                            curr = groupStart
                            print('after finish one group, curr is')
                            print(curr.data)
                        else:
                            return head
                    else:
                        grouplast.next = curr.next
                        curr.next.next = curr
                        curr.next = None
                        return head

                else:
                    return head
            return head

    # This is a neater solution from Discussion, it only work on two nodes as a group once
    # It can be confusing that return dummy.next is returning the head node of the original linked list
    # Just follow the comments below to find out why return dummy.next is actually correct
    # refer to https://www.youtube.com/watch?v=naG4uXpmVAU to learn more about object, address, variables and stuff in Python

    def swapPairs1(self, head):
        # so here dummy and p are initialized to store the adress of Node(0)
        dummy = p = Node(0)
        # changing dummy.next is actually changing Node(0).next, so p.next is also changed
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            # same logic applies here, changing p.next is actually changing Node(0).next, so dummy.next is also changed
            p.next = tmp
            head = head.next
            # however, from now on, p doesn't store the address of Node(0) anymore
            # so from now on, change p.next will not affect dummy.next
            p = tmp.next
        return dummy.next

firstNode = Node(2)
secondNode = Node(5)
thirdNode = Node(3)
forthNode = Node(4)
fifthNode = Node(6)
sixthNode = Node(2)
seventhNode = Node(2)
eightthNode = Node(3)
ninthNode = Node(4)
tenthNode = Node(5)
eleventhNode = Node(6)
linkedList1 = LinkedList()
linkedList1.insertEnd(firstNode)
linkedList1.insertEnd(secondNode)
linkedList1.insertEnd(thirdNode)
linkedList1.insertEnd(forthNode)
linkedList1.insertEnd(fifthNode)
linkedList1.insertEnd(sixthNode)
linkedList1.insertEnd(seventhNode)

#linkedList1.printList()


ans = linkedList1.swapPairs1(linkedList1.head)
ansList = LinkedList()
ansList.insertEnd(ans)
#ansList.printList()