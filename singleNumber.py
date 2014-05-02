class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = None
        for i in A:
            if result is None:
                result = i
            else:
                result ^= i
        return result

s = Solution()
print s.singleNumber([5,2,2,3,3])