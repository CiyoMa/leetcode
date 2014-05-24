class Solution:
    # @return a boolean
    def isValid(self, s):

    	stack = []
        for char in s:
        	if char in ['(', '[', '{']:
        		stack.append(char)
        	else:
        		if len(stack) == 0:
        			return False
        		left = stack.pop()
        		if left == '{' and char == '}' or left == '(' and char == ')' or left == '[' and char == ']':
        			continue
        		else:
        			return False
        return len(stack) == 0

s = Solution()
print s.isValid("]]")
