class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
    	if len(word2) * len(word1) == 0:
    		return max(len(word1), len(word2))
        metrics = [["invalid" for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        metrics[0] = range(len(word2) + 1)
        for i in range(len(metrics)):
        	metrics[i][0] = i
        #print metrics
        for i in range(1, len(metrics)):
        	for j in range(1, len(metrics[i])):
        		if word1[i-1] == word2[j-1]:
        			metrics[i][j] = min(metrics[i-1][j-1], metrics[i-1][j] + 1, metrics[i][j-1] + 1)
        		else:
        			metrics[i][j] = min(metrics[i-1][j-1], metrics[i-1][j], metrics[i][j-1]) + 1
        # for i in metrics:
        # 	print i
        return metrics[len(word1)][len(word2)]

s = Solution()
print s.minDistance('plasma', 'altruism')