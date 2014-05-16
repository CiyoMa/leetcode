# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
    	if head is None:
    		return head
    	before = None
        toSort = head
        next = toSort.next
        while toSort:
        	p = head
        	last = None
        	while p != toSort and p != next:
        		if p.val > toSort.val:
        			if last:
        				last.next = toSort
        			else:
        				head = toSort
        			if before:
        				before.next = next
        			toSort.next = p
        			break
        		last = p
        		p = p.next
        	if p == toSort:
        		before = toSort
        	toSort = next
        	if next:
        	   	next = next.next
        	# h = head
        	# while h:
        	# 	print h.val,
        	# 	h = h.next
        	# print 
        return head

s = Solution()
h = None
tail = None
for i in [-1,4,-3,2,1,5,6] * 200:
	if not h:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next
h = s.insertionSortList(h)
while h:
	print h.val,
	h = h.next







