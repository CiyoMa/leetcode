class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
    	result = []
    	lastRow = None
        for i in range(1, numRows+1):
        	row = [1 for j in range(i)]
        	for j in range(1,i-1):
        		row[j] = lastRow[j-1] + lastRow[j]
        	lastRow = row
        	result.append(lastRow)
        return result

s = Solution()
print s.generate(5)