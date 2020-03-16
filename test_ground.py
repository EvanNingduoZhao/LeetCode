# for i in range(6):
#     print(i)

# l=['s','p','s','b']
# s=str(l)
#
# print(2**3)
#
# for _ in range(5):
#     print('!')

# b=a=[[1,2,3]]
# b=a
# a[0][0]=2
# a[0][0]=10
# print(b)

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



# secondNode = Node(5)
# thirdNode = Node(10)
# forthNode = Node(20)
# import copy
# p = Node(2)
# p.data=[0,0,0]
# print('id of p',id(p))
# dummy = p
# print('id of dummy',id(dummy))
# p.data[1]=1
# print(p.data)
# print(dummy.data)

love = [1,2,3]
print('id of [1,2,3]',id([1,2,3]))
#love = 2
print('id of love',id(love))


def foo(a):
    a[2] = "nothing"

bar = ['You', 'know', 'something', 'Jon', 'Snow']
foo(bar)
print(bar)


print('LLLLLllkkkkkkkkkkkkkkk')
print(7//3)

list1 = [1,2,3]
print(list1)
list1.append(None)
print(list1)

a='1234'
print(a[::-2])