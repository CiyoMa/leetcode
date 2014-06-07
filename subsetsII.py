class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def helper(start,result):
        	if start == len(S):
        		return [[]]
        	i = start+1
        	while i < len(S) and S[i] == S[i-1]:
        		i += 1
        	i -= 1
        	result = []
        	res = helper(i+1, result)
        	#print res,S[start],'#',i-start
        	for i in range(1, i-start+2):
        	   	for j in res:
        	   		result.append([S[start]]*i+j)
        	#visited[start] = False

        	return result+res

        S.sort()
        return helper(0,[])

s = Solution()
print s.subsetsWithDup([1,2,2,3])
