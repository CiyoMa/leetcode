"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution:
    # @return a string
    def countAndSay(self, n):
    	# if n == 1:
    	# 	return '1'
    	next = '1'
    	current = '1'
    	ones = 1
    	twos = 0
    	i = 1
    	while i < n:
    		next = ''
    		last = ''
    		count = 0
    		for char in current:
    			if last == '':
    				last = char
    				count += 1
    				continue
    			if char != last:
    				next += str(count)+last
    				last = char
    				count = 1
    				continue
    			count += 1

    		if count != 0:
    			next += str(count) + last 
    		current = next
    		#print next
    		i += 1
    	return next

s = Solution()
print s.countAndSay(5)