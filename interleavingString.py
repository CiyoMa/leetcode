class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
    	def recursive(p1,p2,p3,l1,l2,memo):
    		if (p1,p2) in memo:
    			return memo[(p1,p2)]
    		if p1 == l1:
    			memo[(p1,p2)] = s3[p3:] == s2[p2:]
    			return memo[(p1,p2)]
    		elif p2 == l2:
    			memo[(p1,p2)] = s3[p3:] == s1[p1:]
    			return memo[(p1,p2)]
    		#print s1[p1], s2[p2], s3[p3]

    		if s1[p1] == s2[p2] and s1[p1] == s3[p3]:
    			temp = recursive(p1+1, p2, p3+1, l1, l2, memo) or recursive(p1,p2+1,p3+1,l1,l2, memo)
    		elif s1[p1] == s3[p3]:
    			temp = recursive(p1+1, p2, p3+1, l1, l2, memo)
    		elif s2[p2] == s3[p3]:
    			temp = recursive(p1, p2+1, p3+1, l1, l2, memo)
    		else:
    			temp = False
    		memo[(p1,p2)] = temp
    		return temp

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l3 != l1 + l2:
        	return False
        return recursive(0,0,0,l1,l2,{})

# TO DO: TRY BOTTOM UP

        # p1, p2, p3 = 0, 0, 0
        # while p1 < l1 and p2 < l2:
        # 	print s1[p1], s2[p2], s3[p3],
        # 	if s3[p3] == s1[p1]:
        # 		print 'p1'
        # 		p1 += 1
        # 	elif s3[p3] == s2[p2]:
        # 		print 'p2'
        # 		p2 += 1
        # 	else:
        # 		return False
        # 	p3 += 1
        # print s1[p1:], s2[p2:], s3[p3:]
        # if p1 < l1:
        # 	return s1[p1:] == s3[p3:]
        # else:
        # 	return s2[p2:] == s3[p3:]

s1, s2, s3 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa", "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab", "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
#"aabcc", "dbbca", "aadbbcbcac" #"aadbbbaccc"
s = Solution()
print s.isInterleave(s1, s2, s3)