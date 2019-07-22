# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0 #carry设置成为0或1的数值，直接用把自己加上去的方式传递是否进位的信息，避免了再用if else去判断的麻烦
        root=cur=ListNode(0) #construct a node using the ListNode constructor
        #只有l1的值、l2的值和进位值只要有一者存在，就需要进行一次计算，把结果存在下一个node里
        while l1 or l2 or carry ==1:
            v1=v2=0 #先把v1和v2设置为0，这样只有在l1或l2对应位置有值时，该值才会被更新并加到sum里
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            sum=v1+v2+carry
            if sum <10:
                # This is how to construct a node
                # and add it to the end of the linked list
                cur.next=ListNode(sum)
                cur=cur.next
                carry=0
            else:
                cur.next=ListNode(sum-10)
                cur=cur.next
                carry=1
        return root.next