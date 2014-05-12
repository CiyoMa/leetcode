# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
    	head = None
    	tail = None
    	nonNonePointers = [l for l in lists if l]
    	while len(nonNonePointers) > 0:
    		minimum = 0
    		temp = []
    		for i in range(len(nonNonePointers)):
    			if nonNonePointers[i].val < nonNonePointers[minimum].val:
    				minimum = i
    		m = nonNonePointers[minimum]
    		nonNonePointers[minimum] = nonNonePointers[minimum].next
    		if nonNonePointers[minimum] is None:
    			del nonNonePointers[minimum]
    		if head is None:
    			head = m
    			tail = m
    		else:
    			tail.next = m
    			tail = tail.next
        return head

n1 = ListNode(5)

n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(4)
n2.next = n3
n3.next = n4

s = Solution()
h = s.mergeKLists([n1,n2])
while h:
	print h.val,
	h = h.next