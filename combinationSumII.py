class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        def helper(num, target, start, visited):
        	#print start
        	if start <= len(num) and target == 0:
        		#print '!'
        		return [[]]
        	elif start > len(num) or target < 0:
        		return None
        	result = set()
        	for i in range(start,len(num)):
        		#if i > 0 and num[i] == num[i-1] and visited[i-1]:
        		#	continue
                # #change to while and move this to the tail of the loop

        		#visited[i] = True
        		residual = target - num[i]
        		if residual < 0:
        		 	return [list(i) for i in list(result)]
        		# print '#',residual, num[i]
        		temp = helper(num,residual, i+1,visited)
        		#print temp, num[i]
        		if temp:
        			for j in temp:
        				t = [num[i]] + j
        				#print t
        				result.add(tuple(t))
        		# print result
        		#visited[i] = False
        	#print [list(i) for i in list(result)], '!'
        	return [list(i) for i in list(result)]

        candidates.sort()
        #print candidates
        res = helper(candidates, target, 0,[False for i in range(len(candidates))])
        if not res:
        	return []
        else:
        	return res

# Using hashset is cheating..... Rewrite!!

A, t = [4,4,2,1,4,2,2,1,3], 8 #[1],1 #[10,1,2,7,6,1,5], 8

s = Solution()
print s.combinationSum2(A, t)