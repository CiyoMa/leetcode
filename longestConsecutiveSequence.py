class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        n = set(num)
        longest = 0
        while len(n) > 0:
        	t = n.pop()
        	tempLong = 1
        	small = t
        	large = t
        	while small-1 in n:
        		small -= 1
        		tempLong += 1
        		n.remove(small)
        	while large + 1 in n:
        		large += 1
        		tempLong += 1
        		n.remove(large)
        	if tempLong > longest:
        		longest = tempLong
        return longest

s = Solution()
print s.longestConsecutive([100,4,200,1,2,3])

