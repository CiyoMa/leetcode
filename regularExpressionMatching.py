class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        def recur(sStart, pStart, memo):
            #print sStart, pStart
            if (sStart, pStart) in memo:
                return memo[(sStart, pStart)]
            if pStart >= len(p):
                memo[(sStart, pStart)] = sStart >= len(s)
                #print len(s), sStart
                return memo[(sStart, pStart)]
            if pStart < len(p) - 1 and p[pStart+1] == '*':
                while sStart < len(s) and (s[sStart] == p[pStart] or p[pStart] == '.'):
                    if recur(sStart, pStart+2, memo):
                        memo[(sStart, pStart)] = True
                        return True
                    sStart += 1
                dp = recur(sStart, pStart+2, memo)
                memo[(sStart, pStart)] = dp
                return dp
            else:
                dp = sStart < len(s) and (s[sStart] == p[pStart] or p[pStart] == '.') and recur(sStart+1, pStart+1, memo)
                memo[(sStart, pStart)] = dp
                return dp

        return recur(0,0,{})

s = Solution()
string, pattern = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
#"ab", ".*c" #"abbabaaaaaaacaa", "a*.*b.a.*c*b*a*c*" #"aa", "aa"
print s.isMatch(string, pattern)#"a", "ab*c*d"
