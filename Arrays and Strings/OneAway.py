# KEY STEP:
# 3 Cases are possible for the two strings
# (1) The length difference > 1. Return False
# (2) The len diff = 1. Check for more than 1 difference. Also check if extra character is used.
# (3) The len diff = 0. Check if more than 1 difference at any character.
# TC: O(n)
# SC: O(1)

class Solution(object):
	def oneAway(self, p, q):
		if abs(len(p)-len(q)) > 1:
			return False
		elif abs(len(p)-len(q)) == 1:
			if len(p) < len(q):
				p, q = q, p
			i, j, c = 0, 0, 0
			while j < len(q):
				if p[i] != p[j]:
					if p[i+1] != p[j]:
						return False
					i += 1
					c += 1
				i += 1
				j += 1
		else:
			c = 0
			for i, j in zip(p, q):
				if i != j:
					c += 1
		if c < 2:
			if i == len(p)-1:
				return False
			else:
				return True
		else:
			return False
