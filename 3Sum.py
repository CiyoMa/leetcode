"""
Given an array S of n integers, are there elements a, b, c
 in S such that a + b + c = 0? Find all unique triplets in
  the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending 
order. (ie, a <= b <=c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
    	num.sort()
    	#print num
    	l = len(num)
    	i = 0
    	result = []

    	while i < l-2:
    		if i != 0 and num[i] == num[i-1]:
    		# remove duplicate result
    			i += 1
    			continue
    		a = num[i]
    		k = i + 1
    		t = l - 1
    		while k < t:
    			b = num[k]
    			c = num[t]
    			if a+b+c == 0:
    				result.append([a,b,c])
    				k += 1
    				t -= 1
    				# -7,-6,1,2,3,4,5,6 => say k = 2, t = 6, 0=-6+1+5<=2+6, 
    				# so next candidate will be some place between these two.
    				while k<t and num[t] == num[t+1]: t -= 1
    				while k<t and num[k] == num[k-1]: k += 1
    			elif a+b+c > 0:
    				t -= 1
    			else:
    				k += 1
    		i += 1
    	return result#[list(i) for i in list(result)]
    	return list(result)

    # def binarySearch(self,num,start,end,target):
    # 	while start < end:
    # 		mid = (start + end)/2
    # 		if num[mid] == target:
    # 			return True
    # 		elif num[mid] < target:
    # 			start = mid + 1
    # 		else:
    # 			end = mid - 1
    # 	return start <= end and num[start] == target

    # @return a list of lists of length 3, [[val1,val2,val3]]
    # def threeSum(self, num):
    	# TLE
    	# num.sort()
    	# #print num
    	# l = len(num)
    	# i = 0
    	# result = []
    	# while i < l-1:
    	# 	j = i+1
    	# 	while j < l:
    	# 		target = -(num[i] + num[j])
    	# 		flag = False
    	# 		start = j+1
    	# 		end = l-1
    	# 		while start < end:
    	# 			mid = (start + end)/2
    	# 			if num[mid] == target:
    	# 				flag = True
    	# 				break
    	# 			elif num[mid] < target:
    	# 				start = mid + 1
    	# 			else:
    	# 				end = mid - 1
    	# 		flag |= start <= end and num[start] == target
    	# 		if flag: #self.binarySearch(num, j+1, l-1, target):
    	# 			result.append((num[i],num[j],target))
    	# 		j += 1
    	# 	i += 1
    	# return result

    # @return a list of lists of length 3, [[val1,val2,val3]]
    # def threeSum(self, num):
    # 	# ---------- TLE -----------
    # 	#num.sort()
    # 	dic = {}
    # 	result = set()
    # 	for n in num:
    # 		dic[n] = dic.get(n,0) + 1
    # 	l = len(num)
    # 	i = 0
    # 	while i < l:
    # 		j = i+1
    		
    # 		dic[num[i]] -= 1
    # 		while j < l:
    # 			dic[num[j]] -= 1
    # 			target = -(num[i] + num[j])
    # 			if dic.get(target,0) > 0:
    # 			    temp = [num[i], target, num[j]]
    # 			    temp.sort()
    # 			    result.add(tuple(temp))
    # 				# if num[i] > target:
    # 				# 	result.add((target, num[i], num[j]))
    # 				# elif target < num[j]:
    # 				# 	result.add((num[i], target, num[j]))
    # 				# else:
    # 				# 	result.add((num[i], num[j], target))
    # 			dic[num[j]] += 1
    # 			j+= 1
    # 		dic[num[i]] += 1
    # 		i += 1
    # 	return list(result)



s = Solution()
#A = [-7,-1,-13,2,13,2,12,3,-11,3,7,-15,2,-9,-13,-13,11,-10,5,-13,2,-12,0,-8,8,-1,4,10,-13,-5,-6,-4,9,-12,5,8,5,3,-4,9,13,10,10,-8,-14,4,-6,5,10,-15,-1,-3,10,-15,-4,3,-1,-15,-10,-6,-13,-9,5,11,-6,-13,-4,14,-3,8,1,-4,-5,-12,3,-11,7,13,9,2,13,-7,6,0,-15,-13,-11,-8,9,-14,1,11,-7,13,0,-6,-15,11,-6,-2,4,2,9,-15,5,-11,-11,-11,-13,5,7,7,5,-10,-7,6,-7,-11,13,9,-10,-9]
#A = [-1,0,1,2,-1,-4]
#A = [-14,-3,11,-3,12,-1,11,13,5,6,-11,-14,-6,11,-4,-15,3,-15,9,-10,13,-10,-9,-13,-12,12,-7,12,12,3,9,5,-14,-3,9,13,11,5,3,-6,-12,-1,-5,-3,-4,-2,-10,6,-10,14,3,-11,11,10,-9,7,-1,-9,4,-12,2,-2,8,3,3,-6,-7,-1,6,12,8,9,-12,10,-8,-1,-7,-3,12,-9,-12,1,-5,6,-12,-7,-2,2,-8,-13,5,9,-7,-10,-3,11,-1,-3,-13,-10,-14,11,6,-10,6,13,4,7,-13,-6,13,12,10,-15,4,13,-7,9,-8,0,4,4,-6,12,9,-2,0]
#A = [13,14,1,2,-11,-11,-1,5,-1,-11,-9,-12,5,-3,-7,-4,-12,-9,8,-13,-8,2,-6,8,11,7,7,-6,8,-9,0,6,13,-14,-15,9,12,-9,-9,-4,-4,-3,-9,-14,9,-8,-11,13,-10,13,-15,-11,0,-14,5,-4,0,-3,-3,-7,-4,12,14,-14,5,7,10,-5,13,-14,-2,-6,-9,5,-12,7,4,-8,5,1,-10,-3,5,6,-9,-5,9,6,0,14,-15,11,11,6,4,-6,-10,-1,4,-11,-8,-13,-10,-2,-1,-7,-9,10,-7,3,-4,-2,8,-13]
#A = [-13,10,11,-3,8,11,-4,8,12,-13,5,-6,-4,-2,12,11,7,-7,-3,10,12,13,-3,-2,6,-1,14,7,-13,8,14,-10,-4,10,-6,11,-2,-3,4,-13,0,-14,-3,3,-9,-6,-9,13,-6,3,1,-9,-6,13,-4,-15,-11,-12,7,-9,3,-2,-12,6,-15,-10,2,-2,-6,13,1,9,14,5,-11,-10,14,-5,11,-6,6,-3,-8,-15,-13,-4,7,13,-1,-9,11,-13,-4,-15,9,-4,12,-4,1,-9,-5,9,8,-14,-1,4,14]
#A = [2,-8,8,6,-14,-12,11,-10,13,14,7,3,10,-13,3,-15,7,3,-11,-8,4,5,9,11,7,1,3,13,14,-13,3,-6,-6,-12,-15,-12,-9,3,-15,-11,-6,-1,0,11,2,-12,3,-6,6,0,-6,-12,-10,-12,6,5,-4,-5,-5,-4,-11,13,5,-2,-13,-3,-7,-15,8,-15,12,-13,0,-3,6,9,-8,-6,10,5,9,-11,0,7,-15,-8,-3,-4,-6,7,7,-2,-2,-11,3,0,-6,12,0,-13,4,-3,11,-11,1,2,13,8,4,9,-1,-2,5,14,12,5,13,-6,-13,-8,9,1,5,-8,-2,-6,-1]
#A = [12,0,3,-14,5,-11,11,-5,-2,-1,6,-7,-10,1,4,1,1,9,-3,6,-15,0,6,1,6,-12,3,7,11,-6,-8,0,9,3,-7,-1,7,-10,1,13,-4,-7,-9,-7,9,3,1,-13,-3,13,8,-11,-9,-8,-3,4,-13,7,-11,5,-14,-4,-9,10,6,-9,-6,-9,-12,11,-11,-9,11,-5,0,-3,13,-14,-1,-13,7,-7,14,5,0,-4,-6,-6,-11,-2,14,-10,2,12,8,-7,-11,-13,-9,14,5,-5,-9,1,-2,6,5,-12,-1,-10,-9,-9,-10,12,11]
A = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]

import time
t = time.time()
#print s.threeSum(A)
s.threeSum(A)
print (time.time() - t) * 1000000