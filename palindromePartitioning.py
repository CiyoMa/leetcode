class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
    	def isPalidrome(start, end):
    		while start < end:
    			if s[start] != s[end]:
    				return False
    			start += 1
    			end -= 1
    		return True

        def dfs(start):
        	if start >= len(s):
        		return [ [] ]
        	result = []
        	for i in range(start, len(s)):
        		if isPalidrome(start, i):
        			res = dfs(i+1)
        			for j in res:
        				result.append([s[start:i+1]] + j)
        	return result
        if len(s) == 0:
        	return []
        return dfs(0)

s = Solution()
print s.partition("aaa")