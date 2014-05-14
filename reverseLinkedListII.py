# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head is None or m == n:
        	return head
        p = head
        i = 1
        last = None
        while i < m:
        	last = p
        	p = p.next
        	i += 1
        p_copy = p
        i = 0
        q = p.next
        while i < n-m:
       		t = q.next
       		q.next = p
       		p = q
        	q = t
        	i += 1

        if last is not None:
        	last.next = p
        else:
        	head = p
        p_copy.next = q
        return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
s = Solution()
h = s.reverseBetween(n1,1,5)
while h:
	print h.val,
	h = h.next



