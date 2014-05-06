class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        c = 0
        l = len(a) - 1
        m = len(b) - 1
        result = ''
        while l >= 0 and m >= 0:
        	# print l, m
        	count = 0
        	if a[l] == '1':
        		count += 1
        	if b[m] == '1':
        		count += 1
        	if c == 1:
        		count += 1

        	if count == 3:
        		result = '1' + result
        		c = 1
        	elif count == 2:
        		result = '0' + result
        		c = 1
        	elif count == 1:
        		result = '1' + result
        		c = 0
        	else:
        		result = '0' + result
        		c = 0
        	l -= 1
        	m -= 1
        # print l, m, c
        if l == m and c == 1:
        	return '1' + result

        if c == 0:
        	return a[:(l + 1)] + b[:(m + 1)] + result
        if l >= 0:
        	return self.addBinary(a[:(l+1)], '1') + result
        elif m >= 0:
        	return self.addBinary(b[:(m+1)], '1') + result
        

s = Solution()
print s.addBinary("111", "10")


