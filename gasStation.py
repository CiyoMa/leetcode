"""
There are N gas stations along a circular route, where the amount of gas at 
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to 
travel from station i to its next station (i+1). You begin the journey with 
an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit 
once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
    	residual = [gas[i] - cost[i] for i in range(len(gas))]
    	if sum(residual) < 0:
    		return -1
    	best = -1
    	temp = 0
    	for i in range(len(gas)):
    		temp += residual[i]
    		if temp < 0:
    			temp = 0
    			best = i

    	return best+1




    	start = [0 for i in range(len(gas))]
    	end = [0 for i in range(len(gas))]
    	temp = 0
    	for i in range(len(gas)):
    		start[i] = temp
    		temp += residual[i]
    	temp = 0
    	for i in range(len(gas)-1,-1,-1):
    		temp += residual[i]
    		end[i] = temp
    	#print residual, start, end
    	for i in range(len(gas)):
    		if start[i] <= 0 and abs(start[i]) <= end[i] and residual[i]>=0:
    			return i
    	return -1


    	# Naive Way - TLE
    	#
        # n = len(gas)
        # for start in range(n):
        # 	total = gas[start]
        # 	#print total, '@'
        # 	next = (start + 1) % n
        # 	flag = True
        # 	while next != start:
        # 		total -= cost[next]
        # 		if total < 0:
        # 			flag = False
        # 			break
        # 		total += gas[next]
        # 		next = (next + 1) % n

        # 	if flag == False:
        # 		#print start,"#"
        # 		continue

        # 	if total >= cost[next]:
        # 		return start
        # return -1

s = Solution()
gas = [1,2]
costs = [2,1]
gas, costs = [1,2,3,3], [2,1,5,1]#[2,4], [3,4]#[2,3,1],[1,4,1]
print s.canCompleteCircuit(gas, costs)
