"""
There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time 
complexity should be O(log (m+n)).
"""

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
    	# @ A should have shorter length than B
    	def findKth(k, shortStart, shortEnd, longStart, longEnd):
    		if shortStart > shortEnd:
    			return B[longStart+k-1]
    		if longStart > longEnd:
    			return A[shortStart+k-1]

    		i = min(k/2 + shortStart, len(A)-1)
    		j = k-(i+1) + longStart #- 1
    		
    		print k, i
    		print i,j
    		if A[i] == B[j]:
    			return A[i]
    		elif A[i] < B[j]:
    			return findKth(k-i-1, shortStart+i+1, shortEnd, longStart, longEnd)
    		else:
    			return findKth(k-i-1, shortStart, shortEnd, longStart+j+1, longEnd)


    	if len(A) > len(B):
    			A, B = B, A
    	return findKth(2,0,len(A)-1,0,len(B)-1)

A = [1,2]
B = range(5)
# A, B = [1], [1]
s = Solution()
print s.findMedianSortedArrays(A,B)