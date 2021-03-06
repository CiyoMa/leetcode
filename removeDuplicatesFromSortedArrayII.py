"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 2:
        	return n
        last = 0
        i = 1
        flag = False
        while i < n:
        	if A[i] != A[last]:
        		flag = False
        		A[last + 1] = A[i]
        		last += 1
        	elif not flag and A[i] == A[last]:
        		flag = True
        		A[last + 1] = A[i]
        		last += 1
        	i += 1
        return last + 1

s = Solution()
A = [1,1,1,2,2,3]
print A[:s.removeDuplicates(A)]




