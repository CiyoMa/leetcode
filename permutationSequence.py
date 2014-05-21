"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

class slot:
	def __init__(self, n):
		self.n = n
		self.data = [str(i+1) for i in range(n)]
		#print self.data

	def getKthSmallest(self, k):
		if k > self.n:
			raise Exception("Given K > n, overflow!")
		i = 0
		count = 0
		while i < self.n and count < k:
			#print self.data[i],i,count,k,self.n
			if self.data[i] == '#':
				i += 1
				#print '@'
				continue
			i += 1
			count += 1
		if count != k or self.data[i-1] == '#' :
			raise Exception("No available K, overflow!")
		result = self.data[i-1]
		self.data[i-1] = '#'
		#print '!', self.data
		return result

class Solution:
    # @return a string
    def getPermutation(self, n, k):
    	def ceil(num):
    		if num * 10 - int(num) * 10 > 0:
    			return num + 1
    		return num
    	result = ''
        p = [1 for i in range(n)]
        for i in range(n):
        	if i == 0:
        		continue
        	p[i] = (i+1) * p[i-1]
        s = slot(n)

        while n > 0:
        	#print k, p[n-2],n,
        	a = int(ceil(1.0*k/p[n-2]))
        	# if a == 0:
        	# 	a = 1
        	# print a
        	char = s.getKthSmallest(a)
        	#print '$'+char

        	result += char
        	#print result

        	k = k - (a-1) * p[n-2]
        	# print k
        	# if k == 0:
        	# 	k = n-1

        	n-=1
        #print k
        return result
        #print result
        #print p

s = Solution()
print s.getPermutation(2,2)