class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	delta = [0] + [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        return sum([i for i in delta if i >= 0])

s = Solution()
print s.maxProfit([1,2,5,1,3])