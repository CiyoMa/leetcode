# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    	if head is None:
    		return False
        p1 = head
        p2 = head.next
        while p2 != None and p1 != p2:
        	p2 = p2.next
        	if p2 == None:
        		return False
        	p1 = p1.next
        	p2 = p2.next
        if p1 == p2:
        	return True
        return False

h = None
tail = None
p = None
for i in range(10):
	if h == None:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next
		if i == 4:
			p = tail

#tail.next = p
s = Solution()
print s.hasCycle(h)
