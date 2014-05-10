"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
    	p = head
    	l = 0
    	while p:
    		l += 1
    		tail = p
    		p = p.next

    	if l <= 1 or k % l == 0:
    		return head
    	k = l - k % l
    	
    	t = 1
    	p = head
    	while t < k:
    		t += 1
    		p = p.next
    	newhead = p.next
    	p.next = None
    	tail.next = head
    	#head = newhead
    	return newhead

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
s = Solution()
h = s.rotateRight(n1,1)
while h:
	print h.val,
	h = h.next