class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	delta = [0] + [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        p = delta
        for i in range(1, len(p)):
        	p[i] = max(p[i-1]+p[i], p[i])
        #print p
        return max(p)

s = Solution()
print s.maxProfit([5,4,3,1])