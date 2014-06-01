class ListNode:
    def __init__(self, key, x):
    	self.key = key
        self.val = x
        self.next = None
        self.front = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.table = {}
        self.current = 0
        self.head = None
        self.limit = capacity
        self.tail = None

    # @return an integer
    def get(self, key):
    	table = self.table
    	if key not in table:
    		return -1
    	self.moveFront(table[key])
    	# p = self.head
    	# while p:
    	# 	print p.key, p.val
    	# 	p = p.next

    	return table[key].val


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	table = self.table
    	if key in table:
    		table[key].val = value
    		self.moveFront(table[key])
    		return
    	self.current += 1
    	if self.current <= self.limit:
    		table[key] = ListNode(key, value)
    	else:
    		node = self.tail
    		del table[node.key]
    		node.key = key
    		node.val = value
    		table[key] = node
    	self.moveFront(table[key])

    def moveFront(self, pointer):
    	if pointer is None or pointer.front is None and pointer.next is not None:
    		#print 'ERROR'
    		return

    	pre = pointer.front 
    	next = pointer.next 
    	if pre is not None:
    		# print next,pre.key
    		pre.next = next
    		if next is None:
    			self.tail = pre
    	if next is not None:
    		next.front = pre
    	pointer.front = None
    	pointer.next = self.head
    	if self.head is not None:
    		self.head.front = pointer
    	if pointer.next is None:
    		self.tail = pointer
    	self.head = pointer
    	# p = self.head
    	# while p:
    	# 	print p.key, p.val
    	# 	p = p.next

size = 2
ops = '[set(2,1),set(3,2),get(3),get(2),set(4,3),get(2),get(3),get(4)]'
ops = ops[1:len(ops)-1]
print ops
import re
ops = re.compile('(?<=\)),').split(ops)
for i in range(len(ops)):
	ops[i] = 'lru.' + ops[i]
# print ops

result = []
lru = LRUCache(size)
for op in ops:
	temp = eval(op)
	# print op,
	# if lru.tail is not None:
	# 	print lru.tail.key, lru.tail.val, lru.head.key, lru.head.val
	# else:
	# 	print 'NULL'
	if temp is None:
		continue
	result.append(temp)

print result
# lru.set(2,1)
# lru.set(3,2)
# print lru.get(2)
# print lru.get(3)
# lru.set(4,3)
# print lru.get(2)
# print lru.get(3)
# print lru.get(4)