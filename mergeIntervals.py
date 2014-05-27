# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        lst = list(set([(i.start, i.end) for i in intervals]))
    	if len(lst) <= 1:
    		return [Interval(i[0], i[1]) for i in lst]
        lst.sort()
        lastStart = lst[0][0]
        lastEnd = lst[0][1]
        result = []
        i = 1
        while i < len(lst):
        	if lst[i][0] > lastEnd:
        		flag = True
        		result.append( (lastStart,lastEnd) )
        		lastStart = lst[i][0]
        		lastEnd = max(lst[i][1], lastEnd)
        	else:
        		flag = False
        		lastEnd = max(lst[i][1], lastEnd)
        	i += 1
        result.append( (lastStart,lastEnd) )
        return [Interval(i[0], i[1]) for i in result]

jobs = [[1,4],[2,3]]
jobs = [Interval(i[0], i[1]) for i in jobs]
s = Solution()
for i in s.merge(jobs):
	print i.start, i.end