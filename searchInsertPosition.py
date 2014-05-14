class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        i = 0
        n = len(A)
        while i < n and A[i] < target:
        	i += 1
        return i

A = [1,3,5,6]
target = 0
s = Solution()
print s.searchInsert(A, target)
