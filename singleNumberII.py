"""
Given an array of integers, every element appears three 
times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""
# simulate ternary addition
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        for n in A:
        	twos |= ones & n
        	ones ^= n
        	threes = ones & twos
        	ones &= ~ threes
        	twos &= ~ threes
        return ones

A = [2,2,2,3]
s = Solution()
print s.singleNumber(A)