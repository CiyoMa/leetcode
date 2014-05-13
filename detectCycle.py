# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return str(self.val)

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
    	if head is None:
    		return None
        p1 = head
        p2 = head.next
        while p2 != None and p1 != p2:
            p2 = p2.next
            if p2 == None:
                return None
            p1 = p1.next
            p2 = p2.next
        #print p1, '@'
        if p1 == p2:
            t = head
            # !! Line 18 will not excute so p2 = p2.next 
            p2 = p2.next
            #print t, p2
            while t != p2:
                t = t.next
                p2 = p2.next
                #print t, p2, t != p2
            return t
        return None

h = None
tail = None
p = None
for i in range(10):
    if h == None:
        h = ListNode(i)
        tail = h
    else:
        tail.next = ListNode(i)
        if i == 4:
            p = tail.next
            #print p
        tail = tail.next

 
tail.next = p
k = h
s = set()
while k:
    print k,
    if k not in s:
        s.add(k)
    else:
        print '#',
        break
    k = k.next
print
s = Solution()
#print p
print s.detectCycle(h)
