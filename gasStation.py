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
print s.canCompleteCircuit([2,3,1],[1,4,1])
