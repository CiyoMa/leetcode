# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
    	if len(intervals) == 0:
    		return [newInterval]
    	firstEndAfter = None
    	lastStartBefore = None
    	n = 0
    	firstEnd = False
    	for i in intervals:
    		if i.start <= newInterval.start:
    			lastStartBefore = n
    		if not firstEnd and i.end >= newInterval.end:
    			firstEnd = True
    			firstEndAfter = n
    		n += 1
    	print '#', lastStartBefore, firstEndAfter
    	result = []
    	flag = True
    	for i in range(len(intervals)):
    		if lastStartBefore is not None and i < lastStartBefore:
    			result.append(intervals[i])
    		elif firstEndAfter is not None and i > firstEndAfter:
    			result.append(intervals[i])
    		elif flag:
    			flag = False
    			if lastStartBefore is None and firstEndAfter is None:
    				result.append(newInterval)
    				continue
    			elif lastStartBefore is None:
    				if intervals[firstEndAfter].start <= newInterval.end:
    					result.append(Interval(newInterval.start, intervals[firstEndAfter].end))
    				else:
    					result.append(newInterval)
    					result.append(intervals[firstEndAfter])
    			elif firstEndAfter is None:
    				if intervals[lastStartBefore].end >= newInterval.start:
    					result.append(Interval(intervals[lastStartBefore].start, newInterval.end))
    				else:
    					result.append(intervals[lastStartBefore])
    					result.append(newInterval)
    			else:
    				lastInterval = False
    				if intervals[firstEndAfter].start <= newInterval.end:
    					endTime = intervals[firstEndAfter].end
    				else:
    					endTime = newInterval.end
    					lastInterval = True

    				firstInterval = False
    				if intervals[lastStartBefore].end >= newInterval.start:
    					startTime = intervals[lastStartBefore].start
    				else:
    					startTime = newInterval.start
    					firstInterval = True

    				if firstInterval:
    					result.append(intervals[lastStartBefore])
    				result.append(Interval(startTime, endTime))
    				if lastInterval:
    					result.append(intervals[firstEndAfter])

    	return result

    def printIntervals(self, intervals):
    	for i in intervals:
			print i.start, i.end

l = [[1,3],[6,9]]
l = [[1,2],[3,5],[6,7],[8,10],[12,16]]
l = [[1,5]]
l = [[2,5],[6,7],[8,9]]
interval = Interval(2, 5)
interval = Interval(4, 9)
interval = Interval(2, 7)
interval = Interval(0, 1)
intervals = []
for i in l:
    intervals.append(Interval(i[0], i[1])) 
s = Solution()
result = s.insert(intervals, interval)
for i in result:
	print i.start, i.end
