class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        left = A[:]
        right = A[:]
        n = len(A)
        for i in range(n):
            if i != 0:
                left[i] = max(left[i], left[i-1])
        for i in range(n-2, 0, -1):
            if i != n-1:
                right[i] = max(right[i], right[i+1])
        remain = [min(left[i], right[i]) for i in range(n)]
        #print remain[1:n-1], '#', remain
        #remain = remain[1:n-1]
        trapped = [remain[i] - A[i] for i in range(1,n-1)]
        #print trapped
        #print left, right
        return sum(trapped)

A = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print s.trap(A)