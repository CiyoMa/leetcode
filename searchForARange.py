class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        low = 0
        high = len(A) - 1

        # find lower bound, first target
        lowerBound = -1
        while low <= high:
        	mid = (low + high) / 2
        	if A[mid] == target and (mid == low or mid - 1 >= 0 and A[mid-1] < target):
        		lowerBound = mid
        		break
        	elif A[mid] < target:
        		low = mid + 1
        	else:
        		high = mid - 1

        # find higher bound, last target
        higherBound = -1
        low = 0
        high = len(A) - 1
        while low <= high:
        	mid = (low + high) / 2
        	if A[mid] == target and (mid == high or mid + 1 <= len(A) and A[mid+1] > target):
        		higherBound = mid
        		break
        	elif A[mid] <= target:
        		low = mid + 1
        	else:
        		high = mid - 1

        return [lowerBound, higherBound]

A = [5, 7, 7, 8, 8, 10]
target = 10
s = Solution()
print s.searchRange(A, target)