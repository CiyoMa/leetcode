class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
        	return True
        s = s.lower()
        start = 0
        end = len(s)-1
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        while start < end:
        	if s[start] not in uppercase and s[start] not in lowercase and s[start] not in digits:
        		start += 1
        		continue
        	if s[end] not in uppercase and s[end] not in lowercase and s[end] not in digits:
        		end -= 1
        		continue
        	if s[start] == s[end]:
        		start += 1
        		end -= 1
        	else:
        		return False
        return True

s = Solution()
print s.isPalindrome("ab2a")
print s.isPalindrome("A man, a plan, a canal: Panama")