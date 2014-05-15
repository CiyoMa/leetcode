class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        can = ['invalid' for i in range(n)]
        can[n-1] = True
        for i in range(n-2, -1, -1):
            if i == n-2:
                can[i] = A[i] >= 1
            else:
                #print can
                can[i] = A[i] >= n - 1 - i
                for j in range(1, A[i]+1):
                    if i + A[i] + 1 > n - 1:
                        break
                    can[i] |= can[i+j]
        return can[0]

A = [3,2,1,0,4]
s = Solution()
print s.canJump(A)
                