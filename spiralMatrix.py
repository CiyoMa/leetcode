class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        i = 0
        m = len(matrix)
        if m < 1:
        	return []
        n = len(matrix[0])
        # if n == 1:
        # 	return [i[0] for i in matrix]
        result = []
        while i < m-i and i < n - i:
        	# move right
        	j = i
        	while j < n - i:
        		result.append(matrix[i][j])
        		j += 1

        	# move down
        	j = i + 1
        	while j < m - i:
        		#print j, n-i-1
        		result.append(matrix[j][n-i-1])
        		j += 1

        	# move left
        	j = n - i - 2
        	while m-1-i > i and j > i-1:
        		result.append(matrix[m-1-i][j])
        		j -= 1

        	# move up
        	j = m - i - 2
        	while i < n-i-1 and j > i:
        		result.append(matrix[j][i])
        		j -= 1
        	i += 1
        return result

matrix = [\
 [ 1, 2, 3 ],\
 [ 4, 5, 6 ],\
 [ 7, 8, 9 ],\
 [ 10, 11, 12 ]\
]
matrix = [[1],[2],[3],[4],[5],[6]]
#matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

s = Solution()
print s.spiralOrder(matrix)




