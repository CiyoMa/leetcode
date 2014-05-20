# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
    	if not head or not head.next:
    		#print '!'
    		return head
    	#print head.val
        p = head
        q = head.next
        while q:
        	q = q.next
        	if q:
        		q = q.next
        		p = p.next
        #print p.val
        secondHalf = p.next
        p.next = None
        left = self.sortList(head)
        right = self.sortList(secondHalf)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
    	if l1 is None:
    		return l2
    	elif l2 is None:
    		return l1
        h = None
        tail = None

        while l1 and l2:
        	if l1.val <= l2.val:
        		p = l1
        		l1 = l1.next
        	else:
        		p = l2
        		l2 = l2.next
        	if h is None:
        		h = p
        		tail = p
        	else:
        		tail.next = p
        		tail = tail.next
        	# n = p.next
        	# p.next = None
        	# p = n
        if l1:
        	tail.next = l1
        if l2:
        	tail.next = l2
        return h

    def combine(self, left, right):
    	if left is None:
    		return right
    	elif right is None:
    		return left

    	head = None
    	tail = None
    	flag = True
    	while left and right:
    		if left.val <= right.val:
    			small = left
    			left = left.next
    		else:
    			small = right
    			right = right.next

    		if not head:
    			head = small
    			tail = small
    		else:
    			tail.next = small
    			tail = tail.next

    		tail.next = None

    	if left:
    		tail.next = left
    	if right:
    		tail.next = right
    	return head

h = None
tail = None
for i in range(5,-1,-1):
	if not h:
		h = ListNode(i)
		tail = h
	else:
		tail.next = ListNode(i)
		tail = tail.next

s = Solution()
h = s.sortList(h)
while h:
	print h.val,
	h = h.next

