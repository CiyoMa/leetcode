"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
    	n = len(matrix)
    	# matrix[i][j] -> matrix[j][n-1-i] -> 
    	# matrix[n-1-j][i] -> matrix[n-1-i][n-1-j] -> 
    	# matrix[i][j]
    	k = 0
    	while n-1-k > k:
    		i = k
    		for j in range(k,n-1-k):
    			down = matrix[n-1-j][i] 
    			left = matrix[n-1-i][n-1-j] 
    			up = matrix[j][n-1-i]
    			right = matrix[i][j]
    			matrix[i][j] = down
    			matrix[j][n-1-i] = right
    			matrix[n-1-j][i] = left
    			matrix[n-1-i][n-1-j] = up
    		# print '#', k
    		# for t in matrix:
    		# 	print t

    		k += 1
    	return matrix

s = Solution()
matrix = [\
[1, 2, 3, 4, 5],\
[1, 2, 3, 4, 5],\
[1, 2, 3, 4, 5],\
[1, 2, 3, 4, 5],\
[1, 2, 3, 4, 5],\
]

print '@'
for i in matrix:
	print i
result = s.rotate(matrix)
print '$'
for i in result:
	print i