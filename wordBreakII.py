"""
Given a string s and a dictionary of words dict, add spaces 
in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
    	# def convert(dp, end, l):
    	# 	result = []
    	# 	for i in dp[end]:
    	# 		tail = s[i:end]
    	# 		if i == 0:
    	# 			result += [tail]
    	# 			continue
    	# 		temp = convert(dp, i, l) 

    	# 		for j in range(len(temp)):
    	# 			temp[j] += ' ' + tail
    	# 		result += temp
    	# 	#print end, result
    	# 	return result

        ##### Try DP + DP - DFS (with memorization) ###########


    	################################################################
    	################# SINGLE PASS -- FAIL, For No Result Case, 
    	################# too many interminate result say, waste memory  
    	################################################################
        # dp = [[] if i > 0 else [''] for i in range(len(s)+1)]

        # for i in range(1,len(s)+1):
        # 	for j in range(i):
        # 		#print j,i,#s[j:i],
        # 		tail = s[j:i]
        # 		if len(dp[j]) and tail in dict:
        # 			print True
        # 			if i == len(s):
        # 				BLANK = ''
        # 			else:
        # 				BLANK = ' '
        # 			for k in dp[j]:
        # 				dp[i].append(k+tail+BLANK)
        # 			print dp[i]
        # 			continue
        # 		print
        # #print dp
        # return dp[len(s)]
        #################### FULL ############################

        dp = [[] if i > 0 else [''] for i in range(len(s)+1)]

        for i in range(1,len(s)+1):
        	for j in range(i-1,-1,-1):
        		#print j,i,s[j:i],
        		#tail = s[j:i]
        		if len(dp[j])>0 and s[j:i] in dict:
        			#print True
        			dp[i].append(j)
        			continue
        		#print
        #print dp
        l = len(s)
        if len(dp[l]) <= 0: return []
        resultList = [[] for i in range(l)]
        for i in range(l):
        	for j in dp[i+1]:
        		tail = s[j:i+1]
        		if i == l-1:
        			BLANK = ''
        		else:
        			BLANK = ' '
        		if j == 0:
        			resultList[i].append(tail+BLANK)
        		else:
        			for k in resultList[j-1]:
        				resultList[i].append(k+tail+BLANK)
        #print resultList
        return resultList[l-1]

        return convert(dp, l, l)

st,dic = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#"bbbbbbbbbbbbb", ['b','bb','abc','abce']
s = Solution()
print s.wordBreak(st, dic)