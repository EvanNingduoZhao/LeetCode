# Definition for singly-linked list.

from Linked_list.singlyLinkedList_learning_notes import Node
from Linked_list.singlyLinkedList_learning_notes import LinkedList


# 这个方法非常巧妙 因为如果两个linked list在交叉点之前的node数量不相等的话，没有办法通过两个pointer p1 p2遍历的方法找到
# 交叉点，加入p1的下一个是x，但p2的下一个不是x，无法通过沿着p2往下找的方法找到交叉点，总会错开（想一想）
# 但是一定的是 设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。
#
# 当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；
# 同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。
# 这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。
#
# 如果不存在交点，那么 a + b = b + a，以下实现代码中 l1 和 l2 会同时为 null，从而退出循环。
def getIntersectionNode(headA, headB):
    p1 = headA
    p2 = headB
    while p1 != p2:
        if not p1:
            p1 = headB
        else:
            p1 = p1.next

        if not p2:
            p2 = headA
        else:
            p2 = p2.next
    return p2



# linkedListA = LinkedList()
# linkedListB = LinkedList()
# Node1 = Node(4)
# linkedListA.insertEnd(Node1)
# Node2 = Node(1)
# linkedListA.insertEnd(Node2)
# Node6 = Node(5)
# linkedListB.insertEnd(Node6)
# Node7 = Node(0)
# linkedListB.insertEnd(Node7)
# Node8 = Node(1)
# linkedListB.insertEnd(Node8)
# Node3 = Node(8)
# linkedListA.insertEnd(Node3)
# linkedListB.insertEnd(Node3)
# Node4 = Node(4)
# linkedListA.insertEnd(Node4)
# linkedListB.insertEnd(Node4)
# linkedListA.printList()
# print('he')
# linkedListB.printList()
# Node5 = Node(5)
# linkedListA.insertEnd(Node5)
# linkedListB.insertEnd(Node5)
#
# print('A:')
# linkedListA.printList()
# print('B:')
# linkedListB.printList()







