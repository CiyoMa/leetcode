class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def recur(sStart, pStart, memo):
        	#print sStart, pStart
        	if (sStart, pStart) in memo:
        		return memo[(sStart, pStart)]

        	if sStart >= len(s) and pStart >= len(p):
        		dp = True
        	elif sStart >= len(s):
        		if pStart == len(p) - 1 and p[pStart] == '*':
        			dp = True
        		elif pStart == len(p) - 1:
        			dp = False
        		elif pStart + 1 < len(p) and p[pStart+1] != '*':
        			dp = False
        		else:
        			if pStart + 1 < len(p) and p[pStart+1] == '*':
        				pStart += 1
        			while pStart + 2 < len(p) and p[pStart + 2] == '*':
        				pStart += 2
        			#print pStart
        			dp = pStart == len(p) - 1

        	elif sStart >= len(s):
        		dp = False
        	else:
        		if pStart >= len(p):
        			dp = False
        		else:
        			if pStart < len(p) -1 and p[pStart+1] == '*':
        				dp = recur(sStart, pStart+1, memo)
        			elif p[pStart] == '*':
        				if s[sStart] == p[pStart-1] or p[pStart-1] == '.':
        					dp = recur(sStart+1, pStart, memo)
        					if not dp:
        						dp = recur(sStart, pStart+1, memo)
        					#print dp
        				else:
        					dp = recur(sStart, pStart+1, memo)
        			elif s[sStart] == p[pStart] or p[pStart] == '.':
        				dp = recur(sStart+1, pStart+1, memo)
        			else:
        				dp = False
        	memo[(sStart, pStart)] = dp
        	return dp
        return recur(0,0,{})

s = Solution()
string, pattern = "abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*"
print s.isMatch(string, pattern)#"a", "ab*c*d"
