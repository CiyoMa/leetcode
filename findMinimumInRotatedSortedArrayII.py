class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        def findPivot():
            start = 0
            end = len(num) - 1
            if num[start] < num[end]:
                return None
            while start <= end:
                mid = (start + end) / 2
                if mid+1 < len(num) and num[mid] > num[mid+1]:
                    return mid
                if num[mid] > num[-1]:
                    start = mid + 1
                elif num[mid] < num[0]:
                    end = mid - 1
                elif num[mid] == num[0] and num[0] == num[-1]:
                    left = mid - 1
                    while left >= 0 and num[left] <= num[left+1]:
                        left -= 1
                    
                    if left >= 0:
                        return left
                    else:
                        right = mid + 1
                        while right < len(num) and num[right] >= num[right-1]:
                            right += 1
                        if right >= len(num):
                            return None
                        else:
                            return right-1
                        
        pivot = findPivot()
        if pivot is None:
            return num[0]
        return num[pivot+1]