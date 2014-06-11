class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
    	
        # if divisor == 1:
        # 	return dividend

        negFlag = False
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            negFlag = True

        divisor = abs(divisor)
        dividend = abs(dividend)

        result = 0

        k = 0
        while divisor << k+1 < dividend:
        	k += 1
        #print k,
        while k >= 0:
        	
        	if dividend >= divisor << k:
        		dividend -= divisor << k
        		result += 1<<k

        	while k >= 0 and dividend < divisor << k:
        	    k -= 1
        	    
        # Naive Way:
        # while dividend - divisor >= 0:
        # 	result += 1
        # 	dividend -= divisor

        if negFlag:
        	return 0 - result
        return result 

s = Solution()
print s.divide(0,1)
print s.divide(5,3)
print s.divide(1,-1)
print s.divide(2147483647, 2)