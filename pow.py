class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
    	if n < 0:
    		return 1.0 / self.recursivePow(x, -n)
    	return self.recursivePow(x, n) 

    def recursivePow(self, x, n):
        if n == 0:
        	return 1
        elif n == 1:
        	return x

        if n % 2 == 1:
        	result = x
        else:
        	result = 1
        temp = self.pow(x, n/2)
        return temp * temp * result


s = Solution()
print s.pow(34.00515, -3)
print s.pow(0.1, 3)
