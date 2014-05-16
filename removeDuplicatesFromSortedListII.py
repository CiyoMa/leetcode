"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	if head is None or head.next is None:
    		return head

    	filteredHead = None
    	filteredTail = None
    	tailCandidate = None

    	p = head
    	count = -1
    	while p:
    		next = p.next
    		if tailCandidate and tailCandidate.val != p.val:
    			print '#', tailCandidate.val, p.val
    			if not filteredHead:
    				print "!!!!!!!!!!!"
    				filteredHead = tailCandidate
    				filteredTail = tailCandidate
    			else:
    				filteredTail.next = tailCandidate
    				filteredTail = filteredTail.next
    			tailCandidate = p
    			p.next = None

    		elif not tailCandidate:
    			print '$', p.val
    			tailCandidate = p
    			tailCandidate.next = None
    		else:
    			print '%', tailCandidate.val, p.val
    			while p.next and p.next.val == tailCandidate.val:
    				p = p.next
    			p = p.next
    			if p:
    				next = p.next
    			else:
    				next = None
    			tailCandidate = p
    			if tailCandidate:
    				tailCandidate.next = None

    		p = next

    		h = filteredHead
    		while h:
    			print h.val,
    			h = h.next
    		print

    	if tailCandidate is not None:
    		if not filteredHead:
    			filteredHead = tailCandidate
    		else:
    			filteredTail.next = tailCandidate

    	return filteredHead

s = Solution()
h = None
tail = None
for i in [1,1,2,3]:
	if not h:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next
h = s.deleteDuplicates(h)
while h:
	print h.val,
	h = h.next


        