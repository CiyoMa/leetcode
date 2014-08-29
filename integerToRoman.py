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

        # NAIVE:
        # if num >= 900:
        #   roman += 'CM'
        #   num -= 900
        # elif num >= 500:
        #   roman += 'D'
        #   temp = (num - 500) / 100
        #   num -= 500 + temp * 100
        #   while temp > 0:
        #       roman += 'C'
        #       temp -= 1
        # elif num >= 400:
        #   roman += 'CD'
        #   num -= 400
        # else:
        #   temp = num / 100
        #   num -= temp * 100
        #   while temp > 0:
        #       roman += 'C'
        #       temp -= 1

        # if num >= 90:
        #   roman += 'XC'
        #   num -= 90
        # elif num >= 50:
        #   roman += 'L'
        #   temp = (num - 50) / 10
        #   num -= 50 + temp * 10
        #   while temp > 0:
        #       roman += 'X'
        #       temp -= 1
        # elif num >= 40:
        #   roman += 'XL'
        #   num -= 40
        # else:
        #   temp = num / 10
        #   num -= temp * 10
        #   while temp > 0:
        #       roman += 'X'
        #       temp -= 1

        # if num >= 9:
        #   roman += 'IX'
        # elif num >= 5:
        #   roman += 'V'
        #   temp = (num - 5)
        #   while temp > 0:
        #       roman += 'I'
        #       temp -= 1
        # elif num >= 4:
        #   roman += 'IV'
        # else:
        #   temp = num 
        #   while temp > 0:
        #       roman += 'I'
        #       temp -= 1
        # return roman

s = Solution()
print s.intToRoman(40)