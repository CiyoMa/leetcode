class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def dfs(k,positiveDiagnal,negativeDiagnal,row,column):
            if k == n:
                return [ [] ]
            res = []
            for i in range(n):
                if not positiveDiagnal[k-i] and not negativeDiagnal[k+i] and not row[k] and not column[i]:
                    positiveDiagnal[k-i] = True
                    negativeDiagnal[k+i] = True
                    row[k] = True
                    column[i] = True
                    temp = dfs(k+1, positiveDiagnal, negativeDiagnal, row, column) 
                    config = '.' * i + 'Q' + '.' * (n-i-1)
                    for conf in temp:
                        conf.insert(0, config)
                    if res is None:
                        res = temp
                    else:
                        res += temp
                        #print res
                    positiveDiagnal[k-i] = False
                    negativeDiagnal[k+i] = False
                    row[k] = False
                    column[i] = False
            return res

        return dfs(0,[False for i in range(2*n-1)],[False for i in range(2*n-1)], [False for i in range(n)], [False for i in range(n)])

s = Solution()
print s.solveNQueens(2)
