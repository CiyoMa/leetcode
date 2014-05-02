class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
    	if len(matrix) == 0 or len(matrix[0]) == 0:
    		return False
        l = self.getList(matrix, target, 0, len(matrix)-1)
        if l is None:
        	return False
        start = 0
        end = len(l)-1
        while start <= end:
        	mid = start + end
        	mid /= 2
        	if l[mid] == target:
        		return True
        	elif l[mid] < target:
        		start = mid + 1
        	else:
        		end = mid - 1
        return False


    def getList(self, matrix, target, start, end):
    	if start>end:
    		return None
    	if start == end:
    		return matrix[start] if len(matrix) > start else None
    	mid = (start + end) / 2
    	if matrix[mid][0] <= target and matrix[mid+1][0] > target:
    		return matrix[mid]
    	elif matrix[mid][0] <= target:
    		return self.getList( matrix, target, mid+1, end)
    	else:
    		return self.getList( matrix, target, start, mid-1)

matrix = [\
  [1,   3,  5,  7],\
  [10, 11, 16, 20],\
  [23, 30, 34, 50]\
]
target = 12
matrix = [[1]]
target = 1
s = Solution()
print s.searchMatrix(matrix, target)