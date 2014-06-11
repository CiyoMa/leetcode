class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
    	S.sort()
    	return self.helper(S, 0, [[]])
    def helper(self, S, k, result):
    	if k == len(S):
    		return result
    	temp = []
    	for i in result:
    		t = i[:]
    		t.append(S[k])
    		temp.append(t)
    	result.extend(temp)
    	return self.helper(S, k+1, result)

s = Solution()
print s.subsets([4,0,3])