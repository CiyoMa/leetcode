class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        last = -1
        i = 0
        n = len(A)
        while i < n:
        	if A[i] != elem:
        		A[last+1] = A[i]
        		last += 1
        	#print A
        	i += 1
        return last + 1

s = Solution()
A = [1,1,1,2,2,3,4,5]
l = s.removeElement(A,2)
print l, A[:l]