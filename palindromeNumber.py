class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverse = 0
        original = x
        while x > 0:
            reverse = reverse * 10 + x % 10
            x /= 10
        return original == reverse