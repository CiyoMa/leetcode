class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        n = len(s)-1
        word = ''
        result = ''
        while n >= 0 and s[n] == ' ':
        	n-=1
        flag = True
        while n >= 0:
        	while n >= 0 and s[n] == ' ':
        		n -= 1
        	end =  n + 1
        	while n >= 0 and s[n] != ' ':
        		n -= 1
        	begin =  n + 1
        	if begin < end:
        		if flag:
        			result += s[begin:end] 
        		else:
        			result += ' ' + s[begin:end] 
        	flag = False
        return result#[:-1]

s = Solution()
t = "  The  Sky  Is Blue"
#t = 'b  a '
print '#', s.reverseWords(t),'#'
