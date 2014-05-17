class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        a = m - 1
        b = n - 1
        l = m + n - 1
        while a >= 0 and b >= 0:
        	if A[a] > B[b]:
        		A[l] = A[a]
        		a -= 1
        	else:
        		A[l] = B[b]
        		b -= 1
        	l -= 1
        while b>= 0 :
        	A[l] =B[b]
        	l -= 1
        	b -= 1


