"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution:
    # @return an integer
    def reverse(self, x):
    	result = 0
    	flag = 1
    	if x < 0:
    		flag = -1
    		x = abs(x)
        while x > 0:
        	result *= 10
        	result += x % 10
        	x /= 10
        return flag * result

s = Solution()
print s.reverse(-1065478)

