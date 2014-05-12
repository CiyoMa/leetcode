# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
    	if l1 is None:
    		return l2
    	elif l2 is None:
    		return l1
        h = None
        tail = None

        while l1 and l2:
        	if l1.val <= l2.val:
        		p = l1
        		l1 = l1.next
        	else:
        		p = l2
        		l2 = l2.next
        	if h is None:
        		h = p
        		tail = p
        	else:
        		tail.next = p
        		tail = tail.next
        	# n = p.next
        	# p.next = None
        	# p = n
        if l1:
        	tail.next = l1
        if l2:
        	tail.next = l2
        return h

n1 = ListNode(5)

n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(4)
n2.next = n3
n3.next = n4

s = Solution()
h = s.mergeTwoLists(n1,n2)
while h:
	print h.val,
	h = h.next