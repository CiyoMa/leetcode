"""
Given a string containing only digits, restore it by returning all 
possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
    	def dfs(start, depth):
    		#print start
    		if len(s) - start < 1 or len(s) - start > 3 and depth == 3 or len(s) - start > 1 and len(s) - start <= 3 and depth == 3 and s[start] == '0':
    			return []
    		if len(s) - start <= 3 and depth == 3 and int(s[start:]) >= 0 and int(s[start:]) <= 255:
    			return [ s[start:] ]
    		result = []
    		for i in range(1,4):
    			ip = s[start:start+i]
    			if s[start] == '0' and len(ip) > 1:
    				break
    			#print ip, start, i
    			if len(ip) > 0 and (int(ip) < 0 or int(ip) > 255):
    				continue
    			next = start+i
    			res = dfs(next, depth + 1)
    			# if res == []:
    			# 	print res, '!'
    			# 	continue
    			for r in res:
    				result.append(ip + '.' + r)
    			# print result, '#'
    		return  result
    	return dfs(0,0)

ip = "0000" #"25525511135"
ip = "010010"
s = Solution()
print s.restoreIpAddresses(ip)
