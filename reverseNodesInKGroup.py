"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    def reverseKGroup(self, head, k):
    	if head == None or head.next == None or k == 1:
    		return head

    	newHead = None
    	newTail = None

    	p = head
    	tempHead = None
    	tempTail = None
    	count = 0
    	while p:
    		if count != 0 and count % k == 0:
    			if tempHead:
    				if newHead:
    					newTail.next = tempHead
    					newTail = tempTail
    				else:
    					newHead = tempHead
    					newTail = tempTail
    				tempHead = None
    				tempTail = None
    			else:
    				print p.val,
    				print "Are u kidding me?"
    		count += 1
    		next = p.next

    		if not tempHead:
    			tempTail = p
    		p.next = tempHead
    		tempHead = p
    		p = next

    	if tempHead and count % k != 0:
    		p = tempHead
    		if newHead:
	    		while p:
	    			next = p.next
	    			temp = newTail.next
	    			newTail.next = p
	    			p.next = temp
	    			p = next
	    	else:
	    		while p:
	    			next = p.next
	    			if newHead == None:
	    				newHead = p
	    				newTail = p
	    				p.next = None
	    			else:
	    				p.next = newHead
	    				newHead = p
	    			p = next
    	elif tempHead:
	    	if newHead:
	    		newTail.next = tempHead
	    	else:
	    		newHead = tempHead
	    	newTail = tempTail
    	return newHead

s = Solution()
h = None
tail = None
for i in range(1,3):
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
h = s.reverseKGroup(h, 3)
while h:
	print h.val,
	h = h.next