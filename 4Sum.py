class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
    	num.sort()
    	#print num
    	i = 0
    	result = []
    	while i < len(num)-3:
    		if i > 0 and num[i] == num[i-1]:
    			i += 1
    			continue
    		a = num[i]
    		j = i + 1
    		#print '@', i, j, len(num) - 2
    		while j < len(num)-2:
    			if j > i + 1 and num[j] == num[j-1]:
    				j += 1
    				continue
    			b = num[j]

    			start = j + 1
    			end = len(num) - 1
    			#print '#', start, end

    			while start < end:
    				c = num[start]
    				d = num[end]
    				#print a,b,c,d
    				if a + b + c + d == target:
    					result.append( (a,b,c,d) )
    					start += 1
    					end -= 1
    					while start < end and num[end] == num[end + 1]: end -= 1
    					while start < end and num[start] == num[start - 1]: start += 1
    				elif a + b + c + d > target:
    					end -= 1
    				else:
    					start += 1
    			j += 1
    		i += 1
    	return result



    # TLE
    	# def binarySearch(start, end, target):
    	# 	if start >= end:
    	# 		return start == end and num[start] == target
    	# 	while start <= end:
    	# 		mid = (start + end)/2
    	# 		if num[mid] == target:
    	# 			return True
    	# 		elif num[mid] < target:
    	# 			start = mid + 1
    	# 		else:
    	# 			end = mid - 1
    	# 	return False

    	# dic = {}
    	# for i in num:
    	# 	dic[i] = dic.get(i,0) + 1

     #    num.sort()
     #    result = []
     #    for i in range(len(num)-3):
     #    	dic[num[i]] -= 1 
     #    	if i != 0 and num[i-1] == num[i]:
     #    		continue
     #    	for j in range(i+1, len(num)-2):
     #    		dic[num[j]] -= 1
     #    		if j != i+1 and num[j-1] == num[j]:
     #    			continue
     #    		for k in range(j+1, len(num)-1):
     #    			dic[num[k]] -= 1
     #    			if k != j+1 and num[k-1] == num[k]:
     #    				continue
     #    			goal = target - num[i] - num[j] - num[k]
     #    			if goal >= num[k] and dic.get(goal, 0) > 0:
     #    			# if dic.get(goal, 0) > 0: Wrong for duplicate [-2,0,0,0,2,2]
     #    			# if binarySearch(k,len(num)-1, goal):
     #    			 	result.append( (num[i], num[j], num[k], goal) )
     #    			dic[num[k]] += 1
     #    		dic[num[j]] += 1
     #    	#dic[num[i]] += 1
     #    return result

s = Solution()
#A = [1, 0, -1, 0, -2, 2]
#A = [-497,-473,-465,-462,-450,-445,-411,-398,-398,-392,-382,-376,-361,-359,-353,-347,-329,-328,-317,-307,-273,-230,-228,-227,-217,-199,-190,-175,-155,-151,-122,-102,-97,-96,-95,-87,-85,-84,-73,-71,-51,-50,-39,-24,-19,-1,-1,7,22,25,27,37,40,43,45,51,72,91,97,108,119,121,122,123,127,156,166,171,175,180,203,211,217,218,224,231,245,293,297,299,300,318,326,336,353,358,376,391,405,423,445,451,459,464,471,486,487,488]
A = [-493,-487,-480,-464,-456,-449,-445,-439,-437,-427,-415,-403,-400,-398,-372,-349,-347,-332,-330,-324,-287,-282,-273,-254,-249,-243,-220,-219,-217,-217,-214,-199,-198,-170,-153,-150,-143,-136,-113,-93,-91,-88,-87,-78,-58,-58,-55,-51,-49,-42,-38,-36,-26,0,13,28,54,61,85,90,90,111,118,136,138,167,170,172,195,198,205,209,241,263,290,302,324,328,347,359,373,390,406,417,435,439,443,446,464,465,468,484,486,492,493]
#t = 0
#t = 2251
t = -4437

print s.fourSum(A, t)

