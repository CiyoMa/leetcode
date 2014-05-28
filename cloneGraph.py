import collections

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
    	if node is None:
    		return None
        visited = set()
        frontier = collections.deque()
        frontier.append(node)
        dic = {}
        while len(frontier) > 0:
        	current = frontier.popleft()
        	copy = UndirectedGraphNode(current.label)
        	dic[current] = copy
        	copy.neighbors = current.neighbors[:]
        	visited.add(current)
        	for neighbor in current.neighbors:
        		if neighbor not in visited: #and neighbor not in frontier:
        			frontier.append(neighbor)
        			visited.add(neighbor)
        			# CAN NOT OMMIT THIS !!! Since duplicate edge like 1->4 and 1->4 can be in neighbors

        visited = set()
        frontier = collections.deque()
        frontier.append(dic[node])
        
        while len(frontier) > 0:
        	current = frontier.popleft()
        	current.neighbors = [dic[neighbor] for neighbor in current.neighbors]
        	visited.add(current)
        	for neighbor in current.neighbors:
        		if neighbor not in visited: #and neighbor not in frontier:
        			frontier.append(neighbor)
        			visited.add(neighbor)
        			# CAN NOT OMMIT THIS !!! Since duplicate edge like 1->4 and 1->4 can be in neighbors

        return dic[node]
