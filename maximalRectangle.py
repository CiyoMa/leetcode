"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing all ones and return its area.
"""

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        def largestRectangleArea(height):
            n = len(height)
            largest = 0
            leftMost = [i for i in range(n)]
            rightMost = [i for i in range(n)]
            
            start = len(height) - 2
            while start >= 0:
                if height[start] == 0:
                    start -= 1
                    continue
                lastRight = None
                right = start + 1
                while right < len(height) and height[right] >= height[start]: #and (right is None or lastRight != right):
                    lastRight = right
                    right = rightMost[right]
                    if height[right] > height[start]:
                        lastRight = right
                        right += 1 
                    elif height[right] == height[start]:
                        lastRight = right
                        break
                if lastRight is not None:
                    rightMost[start] = lastRight
                start -= 1

            start = 1
            while start < len(height):
                if height[start] == 0:
                    start += 1
                    continue
                lastLeft = None
                left = start - 1
                while left >= 0 and height[left] >= height[start]: #and (lastLeft is None or lastLeft != left):
                    lastLeft = left
                    left = leftMost[left]
                    if height[left] > height[start]:
                        lastLeft = left
                        left -= 1 
                    elif height[left] == height[start]:
                        lastLeft = left
                        break
                if lastLeft is not None:
                    leftMost[start] = lastLeft
                start += 1

            # print leftMost, rightMost
            for i in range(n):
                largest = max(largest, height[i] * (rightMost[i] - leftMost[i] + 1))
            return largest

        if len(matrix) == 0:
            return 0
        height = [1 if matrix[0][i] == '1' else 0 for i in range(len(matrix[0]))]
        area = largestRectangleArea(height)
        for i in range(1,len(matrix)):
        	for j in range(len(matrix[0])):
        		if matrix[i][j] == '1':
        			height[j] += 1
        		else:
        			height[j] = 0
        	area = max(area, largestRectangleArea(height))
        return area