class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	if len(prices) <= 1:
    		return 0
        delta = [0] + [prices[i] - prices[i-1] for i in range(1, len(prices))]
        p = delta[:]
        for i in range(1, len(prices)):
            p[i] = max(p[i-1]+p[i], p[i])
        futureMax = [0 for i in range(len(prices))]
        futureBest = None
        for i in range(len(prices)-1, -1, -1):
            if futureBest is None or futureBest < prices[i]:
                futureBest = prices[i]
            futureMax[i] = max(futureBest,prices[i])
        bestEarnAfter = [0 for i in range(len(prices))]
        bestEarnAfter[len(prices)-1] = max(0,futureMax[len(prices)-1] - prices[len(prices)-1])
        for i in range(len(prices)-2, -1, -1):
        	bestEarnAfter[i] = max(bestEarnAfter[i+1],futureMax[i] - prices[i])
        # print prices
        # print p
        # print futureMax
        # print bestEarnAfter
        return max([bestEarnAfter[i]+p[i] for i in range(len(prices))])

prices = [1,2,3,4,5,1,2,3]
prices =[1,2]
s = Solution()
print s.maxProfit(prices)
