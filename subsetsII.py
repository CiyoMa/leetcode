class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def helper(start,visited):
        	if start == len(S):
        		return [[]]

        	for i in range(start+1, len(S))





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



