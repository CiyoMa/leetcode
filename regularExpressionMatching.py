class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def recur(sStart, pStart, memo):
        	#print sStart, pStart
        	if (sStart, pStart) in memo:
        		return memo[(sStart, pStart)]

        	if sStart >= len(s) and pStart >= len(p):
        		dp = True
        	elif sStart >= len(s) and (pStart <= len(p) - 1 and p[pStart] == '*' or pStart < len(p) - 1 and p[pStart+1] == '*'):
        		if pStart == len(p) - 1 and p[pStart] == '*':
        			dp = True
        		elif pStart == len(p) - 1:
        			# print 'here'
        			dp = False
        		# elif pStart + 1 < len(p) and p[pStart+1] != '*':
        		# 	print 'here'
        		# 	dp = False
        		else:
        			if pStart + 1 < len(p) and p[pStart+1] == '*':
        				pStart += 1
        			while pStart + 2 < len(p) and p[pStart + 2] == '*':
        				pStart += 2
        			# print pStart, len(p)
        			dp = pStart >= len(p) - 1
        			# print dp

        	elif sStart >= len(s):
        		dp = False
        	else:
        		if pStart >= len(p):
        			dp = False
        		else:
        			if pStart < len(p) -1 and p[pStart+1] == '*':
        				dp = recur(sStart, pStart+1, memo)
        			elif p[pStart] == '*':
        				dp = recur(sStart, pStart+1, memo)
        				# print dp
        				if not dp and (s[sStart] == p[pStart-1] or p[pStart-1] == '.'):
        					dp = recur(sStart+1, pStart, memo)
        					
        			elif s[sStart] == p[pStart] or p[pStart] == '.':
        				dp = recur(sStart+1, pStart+1, memo)
        			else:
        				assert s[sStart] != p[pStart]
        				dp = False
        	# print dp
        	memo[(sStart, pStart)] = dp
        	return dp
        return recur(0,0,{})

s = Solution()
string, pattern = "aaa", "aaaa"#"abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*" #"aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
#"ab", ".*c" #"abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*" #"aa", "aa"
print s.isMatch(string, pattern)#"a", "ab*c*d"
