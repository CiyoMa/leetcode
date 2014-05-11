# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        p = head
        l = 0
        while p:
        	l += 1
        	p = p.next

        if l <= 2:
        	return

        h = l / 2 + l % 2
        p = head
        t = 1
        while t < h:
        	t += 1
        	p = p.next

        backHalfHead = p.next
        p.next = None
        p = backHalfHead
        reverseHead = None
        while p:
        	t = p.next
        	p.next = reverseHead
        	reverseHead = p
        	p = t
        # p = head
        # while p:
        # 	print p.val,
        # 	p = p.next
        # print 
        # p = reverseHead
        # while p:
        # 	print p.val,
        # 	p = p.next
        p = reverseHead
        q = head
        # print 
        while p:
        	t = p.next
        	k = q.next
        	#print '#',p.val, q.val
        	q.next = p
        	p.next = k
        	p = t
        	q = k

        # p = head
        # while p:
        # 	print p.val,
        # 	p = p.next	

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
s = Solution()
s.reorderList(n1)



