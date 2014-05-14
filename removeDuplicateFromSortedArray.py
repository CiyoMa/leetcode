class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 1:
        	return n
        i = 1
        last = A[0]
        count = 0
        lastDistinct = 0
        while i < n:
            if A[i] == last:
               count += 1
            else:
               last = A[i]
               A[lastDistinct+1] = A[i]
               lastDistinct += 1
            i += 1
        # i = n - count - 1
        # t = len(A) - 1

        # while i < t :
        # 	del A[i]
        # 	t -= 1
        	
        return n-count	

A = [i/3 for i in range(10)]
#print A
s = Solution()
print s.removeDuplicates(A)
print A
