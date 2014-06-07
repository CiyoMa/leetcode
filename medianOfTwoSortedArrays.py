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
    		# print k,
    		if k == 1:
    			return min(A[shortStart], B[longStart])

    		i = min(k/2 + shortStart , len(A)) -1
    		j = k/2 - 1 + longStart #k - (i - shortStart + 1) + longStart -1
    		
    		# print k, i
    		# print k,i,j,'#',shortStart,longStart
    		if A[i] == B[j] and i - shortStart + j - longStart == k - 2:
    			return A[i]
    		elif A[i] < B[j]:
    			return findKth(k- (i - shortStart + 1), i+1, shortEnd, longStart, longEnd)
    		else:
    			return findKth(k- (j - longStart + 1), shortStart, shortEnd, j+1, longEnd)


    	if len(A) > len(B):
    			A, B = B, A
    	# C = A + B
    	# C.sort()
    	# print C, C[4], A, B
    	if (len(A) + len(B)) % 2 == 1:
    		return findKth((len(A) + len(B)) / 2 + 1,0,len(A)-1,0,len(B)-1)
    	#print '@'
    	a = findKth((len(A) + len(B)) / 2,0,len(A)-1,0,len(B)-1)
    	# print '$$$'
    	b = findKth((len(A) + len(B)) / 2 + 1,0,len(A)-1,0,len(B)-1)
    	# print '#', a, b
    	return  (a + b) * 0.5


# A = [1,2,3]
# B = range(8)
A, B = [1,2,3,6], [1,2,3,6] #[1,2], [1,2]#[1,2], [3,4]
s = Solution()
print s.findMedianSortedArrays(A,B)