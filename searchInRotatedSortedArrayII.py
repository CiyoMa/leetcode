"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its 
index, otherwise return -1.

You may assume no duplicate exists in the array.
------ II ------
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

"""
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        high = len(A) - 1
        low = 0
        # if high == low and target == A[low]:
        #     return low
        # elif high == low:
        #     return -1

        if A[low] < A[high]:
        	pivot = - 1
        else:
        	pivot = self.findPivot(A)
        #print pivot
        index = -1
        if target > A[high]:
        	high = pivot
        elif pivot != -1 and target > A[-1]:
        	high = pivot
        elif pivot != -1:
        	low = pivot + 1
        #print low, high
        while high >= low:
        	mid = (high + low) / 2
        	if A[mid] == target:
        		#print mid
        		return True
        	elif A[mid] > target:
        		high = mid - 1
        	else:
        		low = mid + 1
        return False

    def findPivot(self, A, ):
    	low, high = 0, len(A) - 1
        while high >= low:
            mid = (high + low) / 2
            #print low, high, mid, A[mid], '#',
            if mid + 1 < len(A) and A[mid] > A[mid + 1]:
                #print A[mid]
                return mid
            elif mid > 0 and A[mid] < A[mid - 1]:
                return mid - 1
            elif A[low] == A[high]:
                #low += 1
                #high -= 1
                #print high, low
                tempHigh = high
                tempLow = low
                x = A[low]
                while tempHigh >= 0 and A[tempHigh] == x:
                    if tempHigh -1 >= 0 and A[tempHigh] < A[tempHigh - 1]:
                        return tempHigh - 1
                    tempHigh -= 1
                while tempLow <= len(A)-1 and A[tempLow] == x:
                    if tempLow + 1 <= len(A) - 1  and A[tempLow + 1] < A[tempLow]:
                        return tempLow
                    tempLow += 1
                high = tempHigh
                low = tempLow


            elif A[0] > A[mid]:
                high = mid -1
            else:
                low = mid + 1
        #print 
        return -1

s = Solution()
#A = [4,5,6,7,0,1,2,2.5,2.7,3,3.5,3.9]
A = [4,4,5,5,6,7,0,1,2,2,3,3,4,4]
#A = [1,1,2,2,1]
#A = [1,3,1,1,1,1,1,1]
A = [1]
print s.search(A,0)
