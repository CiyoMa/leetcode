class Solution:
    # @return a string
    def intToRoman(self, num):
    	roman = ""
        while num >= 1000:
        	roman += 'M'
        	num -= 1000

        nines = ['CM', 'XC', 'IX']
        fives = ['D', 'L', 'V']
        fours = ['CD', 'XL', 'IV']
        ones = ['C', 'X', 'I']
        i = 0
        while i < 3 and num > 0:
        	power = 10**(2-i)
        	if num >= 9 * power:
        		roman += nines[i]
        		num -= 9 * power
        	elif num >= 5 * power:
        		roman += fives[i]
        		temp = num / power - 5
        		num -= (5 + temp) * power
        		while temp > 0:
        			roman += ones[i]
        			temp -= 1
        	elif num >= 4 * power:
        		roman += fours[i]
        		num -= 4 * power
        	else:
        		temp = num / power
        		num -= temp * power
        		while temp > 0:
        			roman += ones[i]
        			temp -= 1
        	i += 1
        return roman