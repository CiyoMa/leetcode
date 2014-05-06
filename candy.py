class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
    	if len(ratings) == 1:
    		return 1
    	count = [1 for i in range(len(ratings))]
    	for r in range(len(ratings) - 1):
    		if ratings[r] < ratings[r+1] and count[r]>=count[r+1]:
    			count[r+1] = count[r]+1
    		#print count
    	#print "#"
    	for r in range(len(ratings) - 1, 0, -1):
    		if ratings[r] < ratings[r-1] and count[r-1]<=count[r]:
    			count[r-1] = count[r]+1
    		#print count
    	return sum(count)


s = Solution()
print s.candy([1,3,5])