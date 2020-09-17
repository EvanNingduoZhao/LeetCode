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
        #为什么只需要保证有even和even.next不是None
        #因为我们在一个while loop的iteration里涉及四个node，那么我们必须至少保证第三个Node不是None，
        #这样当我们要access第三个node.next时才不会报错。我们可以发现虽然我们每个while loop的iteration里涉及四个node
        #但是下一个iteration里的第一个node和上一个iteration里的第三个node其实是同一个node
        #即当我们有1 2 3 4 5这个linkedlist时，第一个iteration里，odd是1，even是2，第二个iteration里odd 是3，even是4
        #既然我本次iteration的第一个node是上一次iteration的第三个node，且每次iteration都要保证第三个node是一定不是None
        #因此每次iteration的第一个node也是一定存在的，所以每次iteration之前只需要检查第二个和第三个node是否存在，即
        #even和even.next是否存在
        # 最后我们还需要保证两件事，即结束的时候最后一个odd的next指向第一个even，且最后一个even的next指向None，
        # 因为在method的最后我们mutually make sure了第一件事，所以我们只需要论证第二件事。
        # 第二件事又分为两种情况，
        # 情况1：input linked list一共有偶数个node，那么最后一个even node的next本来就是none
        # 情况2：input linked list一共有奇数个node，如1 2 3 4 5，那么第一个iteration odd是1，even是2
        # 第二个iteration odd是3，even是4，没有第三个iteration因为5后面没有even了。在第二个iteration中
        # even.next=even.next.next，4的next成了4的next.next也就是None，所以也没问题
        # 至此我们证明了，这个code是符合结束的时候最后一个odd的next指向第一个even，且最后一个even的next指向None的
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