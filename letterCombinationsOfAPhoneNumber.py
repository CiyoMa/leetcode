"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
    	# if len(digits) == 0:
    	# 	return []
    	return self.helper(digits,0)

    def helper(self,digits,index):
    	if index > len(digits) - 1:
    		return ['']
    	char = digits[index]
    	res = self.helper(digits,index+1)
    	if char in ['1','0','#','*']:
    		return res
    	elif char == '2':
    		temp = []
    		for j in 'abc':
    			temp += [j+i for i in res]

    	elif char == '3':
    		temp = []
    		for j in 'def':
    			temp += [j+i for i in res]

    	elif char == '4':
    		temp = []
    		for j in 'ghi':
    			temp += [j+i for i in res]

    	elif char == '5':
    		temp = []
    		for j in 'jkl':
    			temp += [j+i for i in res]

    	elif char == '6':
    		temp = []
    		for j in 'mno':
    			temp += [j+i for i in res]

    	elif char == '7':
    		temp = []
    		for j in 'pqrs':
    			temp += [j+i for i in res]

    	elif char == '8':
    		temp = []
    		for j in 'tuv':
    			temp += [j+i for i in res]

    	elif char == '9':
    		temp = []
    		for j in 'wxyz':
    			temp += [j+i for i in res]

    	return temp

s = Solution()
print s.letterCombinations("")


        