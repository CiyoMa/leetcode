"""
Given a non-negative number represented as an array 
of digits, plus one to the number.

The digits are stored such that the most significant 
digit is at the head of the list.
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
    	n = len(digits) - 1
    	c = 1
    	while n >= 0 and c > 0:
    		temp = digits[n]
    		digits[n] = (digits[n] + c)%10
    		c = (temp + c)/10
    		#print c, digits[n]
    		n -= 1
    	if c > 0:
    		digits.insert(0,1)
    	return digits

s = Solution()
print s.plusOne([9,9])
        