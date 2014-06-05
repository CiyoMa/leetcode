"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.
"""

class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
    	i = 0
    	# eliminate begining spaces
    	while i < len(s) and s[i] == ' ':
    		i += 1
    	# for empty string
    	if i == len(s):
    		return False

    	# eliminate ending spaces
    	tail = len(s) - 1
    	while s[tail] == ' ':
    		tail -= 1

    	if i == tail:
    		return s[i] != '.' and s[i] != 'e' and s[i] != 'E'

    	signed = False
    	if s[i] == '-' or s[i] == '+':
    		i += 1
    		signed = True
    	begin = i
    	dot = False
    	e = False
    	hasE = False
    	hasDot = False
    	endValid = None
    	while i <= tail:
    		char = s[i]
    		#print char
    		if char >= '0' and char <= '9':
    			if not e:
    				e = True
    			endValid = True
    		elif char == 'e' or char == 'E':
    			if not e or hasE or begin == i:
    				return False
    			else:
    				hasE = True
    				endValid = False
    		elif char == '.':
    			if hasDot or hasE:
    				return False
    			hasDot = True
    		elif char == '-' or char == '+':
    			if i == begin or (i > begin and (s[i-1] != 'e' and s[i-1] != 'E')):
    				#print '!', s[i-1], i > begin, (s[i-1] != 'e' and s[i-1] != 'E')
    				return False
    		else:
    			return False
    		i += 1
    	if endValid is None:
    		return False
    	return endValid

string = ' 005047e+6 '
s = Solution()
print s.isNumber(string)

