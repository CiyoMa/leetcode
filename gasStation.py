class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
    	
    	# Naive Way
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
