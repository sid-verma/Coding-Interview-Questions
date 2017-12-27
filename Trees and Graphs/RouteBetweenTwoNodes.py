# Given a directed graph, design an algorithm to find out the route between two nodes.
# KEY STEP:
# This is a BFS/DFS Question.
# It is a good idea to discuss the trade-offs between bfs and dfs before implementation

class Node(state):
	self.state = state

class Solution(object):
	
# The DFS Implelemtation (using Recursion
	def checkRouteDFS(graph, start, end):
		if start == end:
			return True
		for node in graph.getNodes():
			node.state = 'UNVISITED'
		if start != None:
			start.state = 'VISITING'
			for node in start.getAdjacentNodes():
				if node == end:
					return True
				if node.state == 'UNVISITED':
					self.checkRouteDFS(graph, node, end)
			start.state == 'VISITED'
		return False

# The BFS Implementation (using Queues)
	def checkRouteBFS(graph, start, end):
		if start == end:
			return True
		q = []
		for node in graph.getNodes():
			node.state = 'UNVISITED'
		start.state = 'VISITING'
		q.append(start)
		while (!len(q) == 0):
			u = q.pop(0) # Equivalent of Dequeue
			if u != None:
				for v in u.getAdjacentNodes(): # Checking all adjacent nodes to u => BFS
					if v.state == 'UNVISITED':
						if v == end:
							return True
						else:
							v.state = 'VISITING'
							q.append(v)
				u.state = 'VISITED'
			return False