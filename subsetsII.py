class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def helper(start,visited,result):
        	if start == len(S):
        		return [[]]

        	visited[start] = True
        	for i in range(start+1, len(S)):
        		if S[i] == S[start]:
        			result.append

        	if start > 0 and S[start] == S[start - 1] and not visited[start - 1]:
        		return helper(start, visited)

        	result = []
        	visited[start] = True
        	res = helper(start + 1, visited)
        	print res,S[start],'#'
        	for j in res:
        		result.append([S[start]]+j)
        	#visited[start] = False

        	return result+res

        S.sort()
        visited = [False for i in range(len(S))]
        return helper(0,visited)

s = Solution()
print s.subsetsWithDup([1,2,2,3])



