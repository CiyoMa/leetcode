"""
Given a string, find the length of the longest substring 
without repeating characters. For example, the longest 
substring without repeating letters for "abcabcbb" is "abc",
which the length is 3. For "bbbbb" the longest substring is "b",
with the length of 1.
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
    	best = 0
    	i = 0
    	voc = {}
    	temp = 0
    	j = -1
    	while i < len(s):
    		if s[i] in voc and voc[s[i]] > j:
    			best = max(best, temp)
    			j = voc[s[i]] 
    			voc[s[i]] = i
    			#voc.clear()
    			temp = i-j
    		else:
    			voc[s[i]] = i
    			temp += 1
    		i += 1
    	#print best, temp
    	return max(best, temp)

#TLE if not using temp = i-j

s = Solution()
t = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
#t = 'abcabcbb'
print s.lengthOfLongestSubstring(t)

        