# find needle in haystack

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        m = len(needle)
        n = len(haystack)

        if m == 0:
        	return haystack
        if n <= m :
        	if needle == haystack:
        		return haystack
        	else:
        		return None

        hashSize = 79
        target  = 0
        for j in [ord(i) for i in needle]:
            target *= hashSize
            target += j
        target %= hashSize

        h = 0
        for i in range(m):
        	h *= hashSize
        	h += ord(haystack[i])
        H = h % hashSize
        i = m
        while i < n:
        	#print i-m,i,haystack[i-m:i],H,target
        	if H == target and needle == haystack[i-m:i]:
        		return haystack[i-m:]
        	
        	h /= hashSize
        	h *= hashSize
        	h += ord(haystack[i])
        	H = h % hashSize
        	i += 1
        return None

s = Solution()
print s.strStr("abcdedef",'de')


