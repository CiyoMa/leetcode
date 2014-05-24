class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        longest = 0
        n = len(s)
        i = 0
        temp = 0
        count = 0
        while i < n:
        	char = s[i]
        	longest = max(longest, temp)
        	if char in ['(', '[', '{']:
        		count += 1
        		stack.append(char)
        	else:
        		count -= 1
        		if len(stack) == 0:
        			i += 1
        			# longest = max(longest, temp)
        			temp = 0
        			continue
        		left = stack.pop()
        		if left == '{' and char == '}' or\
        		   left == '(' and char == ')' or\
        		   left == '[' and char == ']':
        		    temp += 2
        		    i += 1
        		    longest = max(temp, longest)
        		    continue
        	i += 1
        return longest#-len(stack)

s = Solution()
print s.longestValidParentheses("()(()")


