"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p = head
        q = head
        i = 1
        while i < n:
        	p = p.next
        	i += 1
        if p.next is None:
        	head = head.next
        	return head
        t = None
        while p.next:
        	t = q
        	q = q.next
        	p = p.next
        t.next = q.next
        return head

h = None
tail = None
for i in range(10):
	if h is None:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next

p = h
while p:
	print p.val,
	p = p.next
print

s = Solution()
h = s.removeNthFromEnd(h,10)
p = h
while p:
	print p.val,
	p = p.next
print