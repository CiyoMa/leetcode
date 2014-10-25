class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        max_a = ['invalid' for i in range(len(A))]
        min_a = ['invalid' for i in range(len(A))]
        max_index = [i for i in range(len(A))]
        min_index = [i for i in range(len(A))]
        for i in range(len(A)):
            if i == 0:
                max_a[i] = A[0]
                min_a[i] = A[0]
            else:
                min_temp = A[i] * min_a[i-1]
                max_temp = A[i] * max_a[i-1]

                previous_max = min_index[i-1]
                previous_min = max_index[i-1]
                if max_temp >= min_temp:
                    previous_max = max_index[i-1]
                    previous_min = min_index[i-1]
                    
                max_a[i] = max(A[i], max_temp, min_temp)
                min_a[i] = min(A[i], max_temp, min_temp)
                
                if A[i] == min_a[i]:
                    previous_min = i
                if A[i] == max_a[i]:
                    previous_max = i

                max_index[i] = previous_max
                min_index[i] = previous_min
                # print max_index
                # print min_index
                # print max_a
                # print "##"

        temp = max(max_a)
        return temp
        print temp
        for i in range(len(A)):
            if max_a[i] == temp:
                # print max_index[i]
                return A[max_index[i]:i+1]

A = [2,3,-2,4]
s = Solution()
print s.maxProduct(A)