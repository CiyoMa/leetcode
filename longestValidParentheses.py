"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", 
which has length = 4.
"""

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        longest = 0
        n = len(s)
        i = 0
        while i < n:
            char = s[i]
            if char == '(':
                stack.append(i) 
            else:
                # no ( matches extra ), continuity breaks
                if len(stack) == 0:
                    stack.append(i)
                    i += 1
                    continue
                left = stack.pop()

                if s[left] == '(':
                    if len(stack) == 0:
                        temp = i + 1
                    else:
                        temp = i - stack[len(stack)-1]
                        # print temp
                    longest = max(temp, longest)
                    i += 1
                    continue
                # no ( matches extra ), continuity breaks
                stack.append(i)
            i += 1
        return longest

s = Solution()
print s.longestValidParentheses("()()))()(())")


