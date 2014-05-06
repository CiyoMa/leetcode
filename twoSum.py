class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        h = {}
        for i in range(len(num)):
        	h[num[i]] = i
        for i in range(len(num)):
        	if h.get(target - num[i], None) is not None and i != h.get(target - num[i]):
        		index1 = min(i, h.get(target - num[i]))
        		index2 = max(i, h.get(target - num[i]))
        		return (index1 + 1, index2 + 1)

s = Solution()
print s.twoSum([2,11,7,15], 9)