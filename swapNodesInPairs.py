# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        beforeTail = None
        tail = None
        newHead = None
        count = 0
        p = head
        while p:
        	count += 1
        	next = p.next
        	p.next = None
        	if count % 2 == 1:
        		if tail:
        			tail.next = p
        			tail = tail.next
        		else:
        			newHead = p
        			tail = p
        	else:
        		if beforeTail:
        			beforeTail.next = p
        			p.next = tail
        		else:
        			p.next = newHead
        			newHead = p
        		beforeTail = tail 
        		# comment the above line (L 34) move it to L30 
        		# - the nearest if, will transfer the list to 
        		# bouncing list.
        	p = next
        return newHead

s = Solution()
h = None
tail = None
for i in range(5):
	if not h:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next
t = h

while h:
	print h.val,
	h = h.next
print 
h = t
h = s.swapPairs(h)
while h:
	print h.val,
	h = h.next

