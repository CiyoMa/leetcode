# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    def suicide(self):
    	del self


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
    	if head is None: return None
    	t = {}
    	cur = head
    	newHead = None
    	pre = None
    	while cur is not None:
    		newcur = RandomListNode(cur.label)
    		if newHead is None:
    			newHead = newcur
    		newcur.random = cur.random
    		if pre is not None:
    			pre.next = newcur
    		pre = newcur
    		t[cur] = newcur

    		cur = cur.next
    	for i in t:
    		print i, t[i]
    	cur = newHead
    	while cur is not None:
    		if cur.random is not None:
    			cur.random = t[cur.random]
    		cur = cur.next
    	return newHead

s = Solution()

n1 = RandomListNode(1)
n2 = RandomListNode(2)
n3 = RandomListNode(3)
n4 = RandomListNode(4)
n1.random = None
n2.random = n1
n3.random = n4
n1.next = n2
n2.next = n3
n3.next = n4

n1.random = n2
n2.next = None
n2.random = None
#n1 = None
cur = n1
while cur:
	print cur.label,
	if cur.random:
		print "!", cur.random.label, "#"
	else: print
	cur = cur.next

print "---"
cur1 = s.copyRandomList(n1)
cur = n1
n1.suicide()
n2.suicide()
n3.suicide()
n4.suicide()

while cur:
	print cur,
	print cur.label,
	if cur.random:
		print cur.random,
		print "!", cur.random.label, "#"
	else: print
	cur = cur.next
print "deleted"
while cur1:
	print cur1,
	print cur1.label,
	if cur1.random:
		print cur1.random,
		print "!", cur1.random.label, "#"
	else: print
	cur1 = cur1.next
