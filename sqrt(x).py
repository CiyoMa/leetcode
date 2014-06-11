class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        start = 0
        end = x
        while start <= end:
        	mid = start + end
        	mid /= 2
        	if mid * mid <= x and (mid + 1) * (mid + 1) > x :
        		return int(mid)
        	elif mid * mid <= x:
        		start = mid + 1
        	else:
        		end = mid - 1

#use division to avoid multiplication overflow

s = Solution()
print s.sqrt(10) == 3
print s.sqrt(0.9) == 0
print s.sqrt(100) == 10