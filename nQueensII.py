class Solution:
    # @return an integer
    def totalNQueens(self, n):
    	def dfs(k,positiveDiagnal,negativeDiagnal,row,column):
    		if k == n:
    			return 1
    		res = 0
    		for i in range(n):
    			if not positiveDiagnal[k-i] and not negativeDiagnal[k+i] and not row[k] and not column[i]:
    				positiveDiagnal[k-i] = True
    				negativeDiagnal[k+i] = True
    				row[k] = True
    				column[i] = True
    				res += dfs(k+1, positiveDiagnal, negativeDiagnal, row, column) 
    				positiveDiagnal[k-i] = False
    				negativeDiagnal[k+i] = False
    				row[k] = False
    				column[i] = False
    		return res

        return dfs(0,[False for i in range(2*n-1)],[False for i in range(2*n-1)], [False for i in range(n)], [False for i in range(n)])

s = Solution()
print s.totalNQueens(8)
