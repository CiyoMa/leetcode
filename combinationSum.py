"""
Given a set of candidate numbers (C) and a target number (T), find all unique 
combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. 
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        def helper(num, target, start):
        	if start < len(num) and target == 0:
        		#print '!'
        		return [[]]
        	elif start == len(num) or target < 0:
        		return None
        	result = []
        	for i in range(start,len(num)):
        		residual = target - num[i]
        		if residual < 0:
        		 	return result
        		# print '#',residual, num[i]
        		temp = helper(num,residual, i)
        		# print temp, num[i]
        		if temp:
        			for j in temp:
        				t = [num[i]] + j
        				result.append(t)
        		# print result
        	return result

        candidates.sort()
        res = helper(candidates, target, 0)
        if not res:
        	return []
        else:
        	return res

s = Solution()
candidates = [2,3,6,7]
print s.combinationSum(candidates, 7)