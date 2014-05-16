"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n < 1:
        	return []
        matrix = [['invalid' for i in range(n)] for j in range(n)]
        i = 0
        count = 1
        while i < n - i:
        	# move right
        	j = i
        	while j < n - i:
        		matrix[i][j] = count 
        		j += 1
        		count += 1

        	# move down
        	j = i + 1
        	while j < n - i:
        		#print j, n-i-1
        		matrix[j][n-i-1] = count
        		j += 1
        		count += 1

        	# move left
        	j = n - i - 2
        	while n-1-i > i and j > i-1:
        		matrix[n-1-i][j] = count
        		j -= 1
        		count += 1

        	# move up
        	j = n - i - 2
        	while i < n-i-1 and j > i:
        		matrix[j][i] = count
        		j -= 1
        		count += 1
        	i += 1
        return matrix

s = Solution()
for i in s.generateMatrix(2):
	print i