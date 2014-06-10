"""
Given a string s1, we may represent it as a binary tree by partitioning it to 
two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a 
scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces 
a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled 
string of s1.
"""

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        def dp(s1, s2, memo = {}):
            # print s1, s2
            if s1 == s2:
            	return True
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            assert len(s1) == len(s2)
            if len(s1) == 2:
                memo[(s1, s2)] = s1[1] == s2[0] and s2[1] == s1[0]
                return s1[1] == s2[0] and s2[1] == s1[0]
            if s1 == s2:
                memo[(s1, s2)] = True
                return True
            counter = {}
            for char in s1:
                counter[char] = counter.get(char, 0) + 1
            for char in s2:
                counter[char] = counter.get(char, 0) - 1
                if counter[char] < 0:
                    memo[(s1, s2)] = False
                    return False

            # cut can be anywhere except the last position 
            # -- which means the back part of the string is empty
            # s1 = substring before cut + cut [length = cut]/ substring after cut [length = len(s1) - cut]
            # s2 = substring before cut + cut / substring after cut
            #    or substring of first len(s1) - cut chars / remaining cut chars

            for cut in range(len(s1)-1):
                # print cut
                if dp(s1[:cut+1], s2[len(s2)-cut-1:], memo) and dp(s1[cut+1:], s2[:len(s2)-cut-1], memo) \
                   or dp(s1[:cut+1], s2[:cut+1], memo) and dp(s1[cut+1:], s2[cut+1:], memo):
                    memo[(s1, s2)] = True
                    # print cut
                    return True
            # print s1,s2
            memo[(s1, s2)] = False
            return False
        return dp(s1, s2)

s1, s2 = "abcd", "bdac"#"abc", "acb" #"great", "rgtae"
s = Solution()
print s.isScramble(s1,s2)


        