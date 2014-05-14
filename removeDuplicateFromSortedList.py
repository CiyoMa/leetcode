# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
        	return head
        p = head
        q = head.next
        while q:
        	while q and q.val == p.val:
        		q = q.next
        	p.next = q
        	p = q
        return head

h = None
tail = None
for i in range(10):
	if h is None:
		h = ListNode(i/3)
		tail = h
	else:
		tail.next = ListNode(i/3)
		tail = tail.next

p = h
while p:
	print p.val,
	p = p.next
print

s = Solution()
h = s.deleteDuplicates(h)
p = h
while p:
	print p.val,
	p = p.next
print

