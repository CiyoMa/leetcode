class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
    	l = min([len(s) for s in strs])
    	prefix = ""
    	for i in range(l):
    		probe = strs[0][i]
    		flag = sum([1 for s in strs if s[i] != probe]) > 0
    		if flag:
    			return prefix
    		else:
    			prefix += probe
    	return prefix

s = Solution()
print s.longestCommonPrefix(["abc","abcde",'ab'])