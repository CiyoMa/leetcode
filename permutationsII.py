class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        def helper(index):
        	l = len(num) - 1
        	if index > l:
        		return []
        	if index == l:
        		return [[num[l]]]
        	k = l - index

        	result = set()
        	rest = helper(index + 1)
        	for i in range(k+1):
        		for j in rest:
        			temp = j[:]
        			#print temp
        			temp.insert(i, num[index])
        			result.add(tuple(temp))
        	return [list(i) for i in result]
        return helper(0)

# Redo DFS Version

s = Solution()
print s.permuteUnique([3,1,1])