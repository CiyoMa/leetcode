class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        m = ['invalid' for i in range(len(A))]
        m[0] = A[0]
        # m is an array of number, m[i] represent the maximum subArray end with A[i]
        for i in range(1, len(A)):
        	# two choices: from extend m[i-1] to end with A[i], just A[i]
        	m[i] = max(m[i-1] + A[i], A[i])

        t = None
        for i in m:
        	if t == None or t < i:
        		t = i
        return t

s = Solution()
print s.maxSubArray([1,2,3,4,-10,100])