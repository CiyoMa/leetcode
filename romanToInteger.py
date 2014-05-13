class Solution:
    # @return an integer
    def romanToInt(self, s):
        result = 0
        flag = True
        for char in s:
        	if flag and char == 'M':
        		result += 1000