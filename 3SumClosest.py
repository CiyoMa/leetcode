class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
    	# # TLE
    	# num.sort()
    	# #print num
    	# l = len(num)
    	# i = 0
    	# best = None
    	# while i < l-1:
    	# 	j = i+1
    	# 	while j < l:
    	# 		goal = target -(num[i] + num[j])
    	# 		temp = None
    	# 		start = j+1
    	# 		end = l-1
    	# 		#print goal
    	# 		while start < end:
    	# 			mid = (start + end)/2
    	# 			if num[mid] == goal:
    	# 				#temp = goal
    	# 				return target
    	# 				break
    	# 			elif num[mid] < goal:
    	# 				start = mid + 1
    	# 			else:
    	# 				end = mid - 1
    	# 		#print start,end
    	# 		if temp is None or start == end:
    	# 			temp = num[end]
    	# 			# if abs(temp-goal-target) > abs(num[end-1]-goal - target):
    	# 			# 	temp = num[end-1]
    	# 		#print num[i], num[j], temp
    	# 		if temp is not None and (best is None or abs(temp-goal-target) < abs(best - target)):
    	# 			best = temp - goal
    	# 			if best == target:
    	# 				return best
    	# 		j += 1
    	# 	i += 1
    	# return best

        num.sort()
        best = None
        for i in range(len(num)-1):
        	if i > 0 and num[i] == num[i-1]:
        		continue
        	a = num[i]
        	start = i + 1
        	end = len(num) - 1
        	#print '@', i, start, end
        	while start < end:
        		b = num[start]
        		c = num[end]
        		#print num[i],num[start], num[end]
        		# if best and a + 2 * b > target:
        		# 	break
        		# if best and a + 2 * c < target:
        		# 	break
        		if best is None or abs(best - target) > abs(a+b+c - target):
        			#print a,b,c,'#'
        			best = a + b + c
        		if a + b + c > target:
        			end -= 1
        		elif a + b + c < target:
        			start += 1
        		else:
        			return target
        		
        		#end -= 1
        		#while start < end and num[start] == num[start-1]: start += 1
        		#while start < end and num[end] == num[end + 1]: end -= 1
        return best

s = Solution()
A = [-1, 2, 1, -4]
A = [1,1,1,0]
A = [0,2,1,-3]
A = [84,49,-47,-56,13,-3,62,-95,23,38,-97,92,34,68,30,90,41,24,-58,83,96,-99,-40,28,-18,-69,-78,95,-62,45,-66,-71,5,94,-42,-66,27,60,-90,-62,87,-22,56,7,-11,75,53,-16,-7,-19,17,18,-14,43,98,-11,0,80,-82,40,5,37,-94,-14,-62,-82,84,23,-9,-68,37,-23,10,26,-22,-52,14,18,-40,-74,-32,47,-87,-81,-68,34,60,75,93,-28,100,-42,0,-87,60,75,-47,7,-57,-61,-2,-96,-18,-98,-3,25,38,-83,60,-12,-62,78,-41,75,-5,89,-97,-1,87,92,57,93,-83,-67,-76,28,-98,-12,22,-2,54,-67,7,99,100,50,5,84,49,-96,-61,-62,-61,29,-59,43,55,30,-10,-22,50,-32,-81,-42,32,55,-94,84,-90,-71,-10,61,56,94,51,8,54,22,22,31]
A, t = [9,-64,-96,-41,-77,95,84,85,-42,88,-60,84,-92,-67,-76,6,51,13,7,-55,-56,-100,81,-76,17,40,-88,21,80,-76,8,-39,-17,4,72,-75,75,67,-92,10,-4,51,-73,-36,26,6,25,93,64,-68,-89,29,49,51,3,14,-11,31,3,-69,-11,30,87,80,-52,-51,88,-35,-8,-9,-48,86,21,76,-51,87,-19,65,71,21,-23,-28,19,-14,16,-5,80,-55,-75,58,-76,19,-26,-100,95,86,59,96,10,72,65,-22,0,-79,74,32,13,-77,36,-69,62,-14,68,-65,-51,36,46,27,0,88,40,90,37,-25,74,36,-81,23,-93,92,57,25,51,-81,-56,93,-20,15,-14,-63,0,90,81,96,-33,-49,-81,-24,-59,-49,-5,10,23,-14,32,57,-7,-80,58,-94,-27,46,-49,39,74,21,-96,-36,-91,-54,-94,-88,-90,55,-7,4,23,8,-19,79,-67,37,31,46,90,-76,-77,-83,62,-12,-19,-36,0,-14,23,45,25,-18,21,-43,-97,-59,-14,-71,-11,78,33,-73,-23,85,11,2,78,-59,-50,41,20], -271
A, t = [43,75,-90,47,-49,72,17,-31,-68,-22,-21,-30,65,88,-75,23,97,-61,53,87,-3,33,20,51,-79,43,80,-9,34,-89,-7,93,43,55,-94,29,-32,-49,25,72,-6,35,53,63,6,-62,-96,-83,-73,66,-11,96,-90,-27,78,-51,79,35,-63,85,-82,-15,100,-82,1,-4,-41,-21,11,12,12,72,-82,-22,37,47,-18,61,60,55,22,-6,26,-60,-42,-92,68,45,-1,-26,5,-56,-1,73,92,-55,-20,-43,-56,-15,7,52,35,-90,63,41,-55,-58,46,-84,-92,17,-66,-23,96,-19,-44,77,67,-47,-48,99,51,-25,19,0,-13,-88,-10,-67,14,7,89,-69,-83,86,-70,-66,-38,-50,66,0,-67,-91,-65,83,42,70,-6,52,-21,-86,-87,-44,8,49,-76,86,-3,87,-32,81,-58,37,-55,19,-26,66,-89,-70,-69,37,0,19,-65,38,7,3,1,-96,96,-65,-52,66,5,-3,-87,-16,-96,57,-74,91,46,-79,0,-69,55,49,-96,80,83,73,56,22,58,-44,-40,-45,95,99,-97,-22,-33,-92,-51,62,20,70,90], 284
#[1,1,-1,-1,3], -1#[0,0,0],1
import time
t1 = time.time()
#s.threeSumClosest(A, t)
print ( time.time() - t1 ) #* 1000
print s.threeSumClosest(A, t)
