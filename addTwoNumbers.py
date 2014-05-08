# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        l = None
        c = 0
        while p1 and p2:
        	val = p1.val + p2.val + c
        	c = val / 10
        	val = val % 10
        	p = ListNode(val)
        	if l == None:
        		l = p
        		head = p
        	else:
        		l.next = p
        		l = l.next
        	p1 = p1.next
        	p2 = p2.next

        if not p1 and not p2:
        	if c == 1:
        		l.next = ListNode(1)
        	return head

        if c == 0:
        	if p1:
        		l.next = p1
        	else:
        		l.next = p2
        	return head

        while p1 and c == 1:
        	val = p1.val + 1
        	c = val / 10
        	val = val % 10
        	p = ListNode(val)
        	l.next = p
        	l = p
        	p1 = p1.next
        if p1:
           l.next = p1

        while p2 and c == 1:
        	val = p2.val + 1
        	c = val / 10
        	val = val % 10
        	p = ListNode(val)
        	l.next = p
        	l = p
        	p2 = p2.next
        if p2:
            l.next = p2

        if c == 1:
        	l.next = ListNode(1)
        return head

h = ListNode(1)
t = ListNode(9)
hh = h
tt = t
for i in []:
	n = ListNode(i)
	hh.next = n
	hh = hh.next

for i in [9]:
	n = ListNode(i)
	tt.next = n
	tt = tt.next

tt = h
while tt:
	print tt.val,
	tt = tt.next
print
tt = t
while tt:
	print tt.val,
	tt = tt.next
print
s = Solution()
tt = s.addTwoNumbers(h, t)

while tt:
	print tt.val,
	tt = tt.next



