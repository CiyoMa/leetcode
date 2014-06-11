"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
    	slash = False
    	stack = []
    	i = 0
        while i < len(path):
        	char = path[i]
        	if char == '/':
        		if slash:
        			i += 1
        			continue
        		slash = True
        		stack.append(char)
        	elif char == '.':
        		slash = True
        		if i + 1 >= len(path) or path[i+1] == '/':
        			# if len(stack) > 1:
        			# 	stack.pop()
        			i += 2
        			continue
        		elif path[i+1] == '.' and (i+2 >= len(path) or path[i+2] == '/'):
        			i += 3
        			if len(stack) > 1:
        				stack.pop()
        			while stack[len(stack)-1] != '/':
        				stack.pop()
        			# print stack
        			continue
        		else:
        			slash = False
        			while i <len(path) and path[i] == '.':
        				stack.append(path[i])
        				i += 1
        			i-=1
        	else:
        		slash = False
        		stack.append(char)
        	i += 1
        if len(stack) > 1 and stack[len(stack)-1] == '/':
        	return ''.join(stack[:len(stack)-1])
        return ''.join(stack)

path = "/home/foo/./bar/"#'/...'#'///home/.' #'/a/./b/../../c/'
s = Solution()
print s.simplifyPath(path)