class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        def helper(index):
        	l = len(num) - 1
        	if index > l:
        		return []
        	if index == l:
        		return [[num[l]]]
        	k = l - index

        	result = []
        	rest = helper(index + 1)
        	for i in range(k+1):
        		for j in rest:
        			temp = j[:]
        			#print temp
        			temp.insert(i, num[index])
        			result.append(temp)
        	return result
        return helper(0)

s = Solution()
print s.permute([0,1,2])