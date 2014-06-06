class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        n = len(num1)
        m = len(num2)
        temp = ''
        for i in num1:
        	temp = i + temp
        num1 = temp 
        temp = ''
        for i in num2:
        	temp = i + temp
        num2 = temp 
        result = [0 for i in range(n+m+1)]
        # result[0] is dummy
        bit = 0
        c = 0
        for i in num1:
        	if i == '0':
        		bit += 1
        		continue
        	jbit = bit
        	for j in num2:
        		result[jbit] += int(i) * int(j)
        		jbit += 1
        	bit += 1
        #print result
        for i in range(n+m+1):
        	temp = result[i] / 10
        	result[i] %= 10
        	if i < n+m:
        		result[i+1] += temp
        tail = n + m 

        while tail > 0 and result[tail] == 0:
        	tail -= 1
        # if tail == 0:
        # 	return '0'
        temp = ''
        while tail >= 0:
        	temp += str(result[tail])
        	tail -= 1
        return temp


num1, num2 = '98','9'
s = Solution()
print s.multiply(num1, num2)
