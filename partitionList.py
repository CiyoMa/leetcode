# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        less = None
        ltail = None
        geq = None
        gtail = None
        p = head
        while p:
        	q = p.next
        	p.next = None
        	if p.val < x:
        		if less is None:
        			less = p
        			ltail = p
        		else:
        			ltail.next = p
        			ltail = ltail.next
        	else:
        		if geq is None:
        			geq = p
        			gtail = p
        		else:
        			gtail.next = p
        			gtail = gtail.next
        	p = q

        if less:
        	head = less
        	ltail.next = geq
        else:
        	head = geq
        return head


h = None
tail = None
for i in range(10):
	if h is None:
		h = ListNode(i + (-2)**i)
		tail = h
	else:
		tail.next = ListNode(i + (-2)**i)
		tail = tail.next

p = h
while p:
	print p.val,
	p = p.next
print

s = Solution()
h = s.partition(h,4)
p = h
while p:
	print p.val,
	p = p.next
print


