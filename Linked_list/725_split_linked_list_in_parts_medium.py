print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
from singlyLinkedList_learning_notes import Node
from singlyLinkedList_learning_notes import LinkedList

def splitListToParts(root, k):
    #handle base cases
    if k == 0:
        return []
    elif k == 1:
        return [root]
    else:
        length = 0
        current = root
        ans = []
        while current:
            length += 1
            current = current.next
        # when k>= 2 we can have two different cases

        # 1. k is larger then linkedlist length:
        # each non-empty entry of the ans list will be a
        # linkedlist with only the head node and some later slices are empty
        # Eg:
        #Input:  root = [1, 2, 3], k = 5
        #Output: [[1], [2], [3], [], []]

        # 2. k is smaller than linkedlist length:
        # 为了满足两个slice的长度差不超过1，我们需要有length%k个长一些的slice
        # 和k-length%k个短slice 列 10 分3段 只能是 【4 3 3】， 11 分3段则只能是【4，4，3】
        # 10%3=1 所以有一个4 而 11%3=2 所有有两个4

        if length < k:
            current = root

            #放一个node的slice
            while current:
                ans.append(current)
                # 注意我们把每个slice的head放到return list里面后 要把这个slice的最后一个node和它的input
                # linked list里的next之间的联系断掉
                # 在这种情况里每个slice只有一个node
                temp = current.next
                current.next = None
                current = temp

            #放empty的slice
            for i in range(k - length):
                ans.append(None)
            return ans

        else:
            reminder = length % k
            partLength = length//k
            current = root

            # 放长slice
            for i in range(reminder):
                ans.append(current)
                count = 1
                while count < partLength + 1:
                    current = current.next
                    count += 1
                # 这种情况里每个slice有多个node，上述断联系的问题看的更清楚
                temp = current.next
                current.next = None
                current = temp

            #放短slice
            for j in range(k - reminder):
                ans.append(current)
                count = 1
                while count < partLength:
                    current = current.next
                    count += 1
                temp = current.next
                current.next = None
                current = temp

            return ans


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
#testlist.printList()
#print(splitListToParts(testlist.head,3)[2].data)
def printOutput(inputList):
    print('The length of the input list is',len(inputList))
    for i in range(len(inputList)):
        current = inputList[i]
        #print("current.data is ", current.data)
        while current is not None:
            print(current.data)
            current = current.next
        print("***************")

printOutput(splitListToParts(testlist.head,3))