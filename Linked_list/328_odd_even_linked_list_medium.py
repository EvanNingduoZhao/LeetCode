from singlyLinkedList_learning_notes import Node
from singlyLinkedList_learning_notes import LinkedList

# very straightforward solution
def oddEvenList(head):
    if head is None or head.next is None or head.next.next is None:
        return head
    else:
        odd = head
        even = head.next
        evenhead = even
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head

def printfromhead(head):
    current= head
    print('********')
    while current:
        print(current.data)
        current = current.next
    print('********')
Node1= Node(1)
Node2= Node(2)
Node3= Node(3)
Node4= Node(4)
Node5= Node(5)
Node6= Node(6)
Node7= Node(7)
testlist = LinkedList()
testlist.insertEnd(Node1)
testlist.insertEnd(Node2)
testlist.insertEnd(Node3)
testlist.insertEnd(Node4)
testlist.insertEnd(Node5)
testlist.insertEnd(Node6)
testlist.insertEnd(Node7)

oddEvenList(testlist.head)
testlist.printList()