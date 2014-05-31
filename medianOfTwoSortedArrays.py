"""
There are two sorted arrays A and B of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time 
complexity should be O(log (m+n)).
"""

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
    	def findKth(k):

    		n, m = A, B
    		if len(A) > len(B):
    			n, m = B, A
    		i = min(k/2, len(n)-1)

    		j = 


# class Solution:
#     # @return a float
#     def findMedianSortedArrays(self, A, B):
#     	def binarySearchFirstLargerThanTarget(target,array):
#     		start = 0
#     		end = len(array) - 1
#     		while start < end:
#     			mid = (start + end) / 2
#     			if array[mid] >= target and mid > 0 and array[mid - 1] < target:
#     				return mid
#     			elif array[mid] > target:
#     				end = mid - 1
#     			else:
#     				start = mid + 1
#     		if array[start] > target:
#     			return 0
#     		return start + 1

#         def findKth(k):
#         	#rint k, '@'
#         	assert len(A) + len(B) >= k
#         	if len(A) == 0 and len(B) >= k:
#         		return B[k-1]
#         	if len(B) == 0 and len(A) >= k:
#         		return A[k-1]
#         	#oddFlag = (len(A) + len(B)) % 2 == 1
#         	aEnd = len(A) - 1
#         	bEnd = len(B) - 1
#         	aStart = 0
#         	bStart = 0
#         	while aStart <= aEnd:
#         		aMid = (aStart + aEnd) / 2
#         		bIndex = binarySearchFirstLargerThanTarget(A[aMid], B)
#         		left = aMid + bIndex + 1
#         		print aMid, bIndex, left,'@'
#         		if left == k:
#         			#print A[aMid]
#         			return A[aMid]
#         		elif left < k:
#         			aStart = aMid + 1
#         		else:
#         			aEnd = aMid - 1
#         	print 'In B'
#         	while bStart <= bEnd:
#         		bMid = (bStart + bEnd) / 2
#         		aIndex = binarySearchFirstLargerThanTarget(B[bMid], A)
#         		left = bMid + aIndex + 1
#         		if left == k:
#         			#print B[bMid]
#         			return B[bMid]
#         		elif left < k:
#         			bStart = bMid + 1
#         		else:
#         			bEnd = bMid - 1
#         assert len(A) > 0 or len(B) > 0
#         if len(A) == 0:
#         	notZero = B
#         elif len(B) == 0:
#         	notZero = A
#         if len(A) * len(B) == 0:
#         	if len(notZero) % 2 == 1:

#         		return notZero[len(notZero)/2]
#         	else:
#         		return (notZero[len(notZero)/2 - 1] + notZero[len(notZero)/2]) / 2.0
#         oddFlag = (len(A) + len(B)) % 2 == 1
#         if oddFlag:
#         	#print (len(A) + len(B)) / 2 + 1
#         	return findKth((len(A) + len(B)) / 2 + 1)
#         else:
#         	return (findKth((len(A) + len(B)) / 2) + findKth((len(A) + len(B)) / 2 + 1)) / 2.0

A = [1,2]
B = range(5)
A, B = [1], [1]
s = Solution()
print s.findMedianSortedArrays(A,B)