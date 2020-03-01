# tasks to perform:
# create nodes
# create linked list
# add nodes to linked list
# print linked list

# to construct a linked list, we need two classes
# one is the Node class
# the other one is the Linkedlist class

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

    def listLength(self):
        length = 0
        currentNode = self.head
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length


    def insertHead(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temporaryNode = self.head
            self.head = newNode
            self.head.next = temporaryNode

    def insertAt(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("Invalid Position")
            return
        if position == 0:
            self.insertHead(newNode)
            return
        currentPosition = 0
        currentNode = self.head
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1


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

# Node => data, next
firstNode = Node('john')
linkedList = LinkedList()
print('This is the intial state when a Linkedlist instance is just created:')
print(linkedList.__dict__)
linkedList.insertEnd(firstNode)

secondNode = Node("Ben")
linkedList.insertEnd(secondNode)

thirdNode = Node("Matthew")
linkedList.insertHead(thirdNode)

print('This is the state after three nodes were inserted:')
# note that the only attribute of a singly linked list is i ts head
# and in this case the head is an node instance
print(linkedList.__dict__)
linkedList.printList()

linkedList1 = LinkedList()
Node1= Node(10)
Node2 = Node(20)
linkedList1.insertEnd(Node1)
linkedList1.insertEnd(Node2)
Node3 = Node(15)
linkedList1.insertAt(Node3,2)
linkedList1.printList()

linkedList1.insertAt(Node3,100)