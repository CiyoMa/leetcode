class Solution:
    # @return an integer
    def romanToInt(self, s):
    	num = 0
    	i = 0
    	while i < len(s) and s[i] == 'M':
    		num += 1000
    		i += 1

    	convertMap = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    	while i < len(s):
    		if i + 1 < len(s) and s[i] in ['C', 'X', 'I'] and convertMap.get(s[i] + s[i+1], 0) > 0:
    			num += convertMap.get(s[i] + s[i+1], 0)
    			i += 1
    		else:
    			num += convertMap[s[i]]
    		i += 1
    	return num

s = Solution()
print s.romanToInt('MCMXC')