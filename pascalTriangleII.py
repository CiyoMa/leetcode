class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
    	lastRow = None
        rowIndex += 1
        for i in range(1, rowIndex+1):
        	row = [1 for j in range(i)]
        	for j in range(1,i-1):
        		row[j] = lastRow[j-1] + lastRow[j]
        	lastRow = row
        return row

s = Solution()
print s.getRow(3)