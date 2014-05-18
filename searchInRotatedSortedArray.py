"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its 
index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        high = len(A) - 1
        low = 0
        if A[low] <= A[high]:
        	pivot = - 1
        else:
        	pivot = self.findPivot(A)
        index = -1
        if target > A[high]:
        	high = pivot
        elif pivot != -1 and target > A[-1]:
        	high = pivot
        elif pivot != -1:
        	low = pivot + 1
        #print high, low
        while high >= low:
        	mid = (high + low) / 2
        	if A[mid] == target:
        		#print mid
        		return mid
        	elif A[mid] > target:
        		high = mid - 1
        	else:
        		low = mid + 1
        return -1

    def findPivot(self, A, ):
    	low, high = 0, len(A) - 1
        while high >= low:
        	mid = (high + low) / 2
        	if A[mid] >= A[mid - 1] and A[mid] > A[mid + 1]:
        		#print A[mid]
        		return mid
        	elif A[0] > A[mid]:
        		high = mid -1
        	else:
        		low = mid + 1

s = Solution()
A = [4,5,6,7,0,1,2,2.5,2.7,3,3.5,3.9]
print s.search(A,1)
