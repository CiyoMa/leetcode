"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent 
the color red, white, and blue respectively.
"""
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        lastRed = -1
        lastWhite = -1
        i = 0
        l = len(A)
        while i < l:
        	if A[i] == 0:
        		tempAfterWhite = A[lastWhite + 1]
        		tempAfterRed = A[lastRed + 1]
        		A[lastRed + 1] = A[i]
        		A[i] = tempAfterWhite
        		# Case: No white before i
        		if lastRed != lastWhite:
        			A[lastWhite + 1] = tempAfterRed
        		lastRed += 1
        		lastWhite += 1
        		#print '#',
        	elif A[i] == 1:
        		temp = A[lastWhite + 1]
        		A[lastWhite + 1] = A[i]
        		A[i] = temp
        		lastWhite += 1
        		#print '@',
        	i += 1
        	#print i, lastRed, lastWhite, A

A = [0, 1, 0, 1, 2, 1, 0, 2, 1, 2]
#A = [2, 0]
s = Solution()
s.sortColors(A)
print A