class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s == '':
        	return ''
        if nRows == 1:
        	return s
        buff = ['' for i in range(nRows)]
        n = len(s)
        div = nRows + (nRows - 2)
        for i in range(n):
        	temp = i % div
        	#print s[i], temp
        	if temp < nRows:
        		buff[temp] += s[i]
        	else:
        		#print nRows-(temp-nRows)-2
        		buff[nRows-2-(temp-nRows)] += s[i]
        #print buff
        return ''.join(buff)

s = Solution()
print s.convert('PAYPALISHIRING', 3)