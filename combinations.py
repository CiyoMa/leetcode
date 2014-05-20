class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
    	def helper(choices,visited,start):
    		#if choices == 1:
    		#	return [[i+1] for i in range(n)]
    		if choices == 0:
    			return [ [] ]
    		result = []
    		for i in range(start,n):
    			if not visited[i]:
    				visited[i] = True
    				temp = helper(choices-1, visited, i+1)
    				#print temp, start, n
    				
    				for j in temp:
    					t = [i+1] + j
    					result.append(t)
    				visited[i] = False
    		return result

    	visited = [False for i in range(n)]
    	return helper(k, visited, 0)

s = Solution()
print s.combine(4,2)
