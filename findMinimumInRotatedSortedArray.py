class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        def findPivot():
            start = 0
            end = len(num) - 1
            if num[start] <= num[end]:
                return None
            while start <= end:
                mid = (start + end) / 2
                if mid+1 < len(num) and num[mid] > num[mid+1]:
                    return mid
                if num[mid] > num[-1]:
                    start = mid + 1
                elif num[mid] < num[0]:
                    end = mid - 1
        pivot = findPivot()
        if pivot is None:
            return num[0]
        return num[pivot+1]