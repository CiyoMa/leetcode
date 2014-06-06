"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there
exists one unique longest palindromic substring.
"""

#Not Subsequence!!!!!

class Solution:
    # @return a string
    def longestPalindrome(self, s):
    	n = len(s)
    	longest = 1
    	bestLeft = 0
    	bestRight = 0
    	for i in range(n):
    		#even
    		left = i
    		right = i + 1
    		while left >= 0 and right < n and s[left] == s[right]:
    			left -= 1
    			right += 1
    		left += 1
    		right -= 1
    		if right - left + 1 > longest:
    			bestLeft = left
    			bestRight = right
    			longest = right - left + 1
    		#odd
    		left = i - 1
    		right = i + 1
    		while left >= 0 and right < n and s[left] == s[right]:
    			left -= 1
    			right += 1
    		left += 1
    		right -= 1
    		if right - left + 1 > longest:
    			bestLeft = left
    			bestRight = right
    			longest = right - left + 1
    	if longest == 0:
    		return s[0]
    	return s[bestLeft:bestRight+1]


#DP in Python can not get rid of TLE
# class Solution:
#     # @return a string
#     def longestPalindrome(self, s):
#     	def change(i,j):
#     		if j == i or j == i + 1:
#     			return 1
#     		return 0

#     	def dprog(s):
#     		dp = [[change(i,j) for j in range(len(s)+1)] for i in range(len(s))]
#     		longest = 1
#     		start = 0
#     		end = 1
#     		for j in range(1,len(s)):
#     			for i in range(j-1,-1,-1):
#     				if s[i] == s[j] and dp[j-1][i+1] > 0:
#     					dp[j][i] = 1
#     					if j-i+1 > longest:
#     						longest = j-i+1
#     						start = i
#     						end = j+1
#     				else:
#     					dp[j][i] = 0
#     		return s[start:end]#best

#     	return dprog(s)

s = Solution()
st = "abcgggdefggg"
st = "cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"
st = 'bb'
print s.longestPalindrome(st)
        