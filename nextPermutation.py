"""
Implement next permutation, which rearranges numbers into 
the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it 
as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra 
memory.

Here are some examples. Inputs are in the left-hand column 
and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
"""

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if len(num) <= 1:
        	return num
        #num[len(num)-1], num[len(num)-2] = num[len(num)-2], num[len(num)-1]
        i = len(num) - 1
        while i > 0: #and num[i] >= num[i-1]:
        	if num[i] > num[i-1]:
        		t = i 
        		while t < len(num) and num[t] > num[i-1]:
        			t += 1
        		t -= 1
                #num[t] is the last one after num[i] greater than num[i-1] or num[i-1] itself
        	   	num[t], num[i-1] = num[i-1], num[t]
        	   	break
        	i -= 1
        #print i
        print num
        start = i
        end = len(num)-1
        #print end
        while start < end and num[start] != num[end]:
        	num[start], num[end] = num[end], num[start]
        	start += 1
        	end -= 1
        #print num
        return num

A = [1,2,3,4,5]
A = [1,3,5,2,1,0]
#A = [3,2,1]
#A = [1,1,5,1,1,1]
#A = [1,3,2,0]
#A = [1,3,2]
#A = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80,79,78,77,76,75,74,73,72,71,70,69,68,67,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
s = Solution()
print s.nextPermutation(A)
