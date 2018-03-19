# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
# Also given an integer k, you need to output the last day when there exists a consecutive flower set in the status of blooming while flowers beside the set are not blooming.
# If there isn't such day, output -1.

# Example 1:
# Input: 
# flowers: [3,1,5,4,2]
# k: 1
# Output: 4
# Explanation: The 4th day is the last day when there is a flower set of size k = 1

# Example 2:
# Input: 
# flowers: [3,1,5,4,2]
# k: 2
# Output: -1
# Explanation: There is no day when there is a flower set of size k = 2

# Note:
# The given array will be in the range [1, 20000].

def solution(P, K):
	s = 0
	e = K
	pos = ['#']*len(P)
	for i in range(len(P)):
		pos[P[i]-1] = i+1
	ans = []
	for i in range(len(pos)):
		# print(max(pos[s:e]))
		if s == 0:
			if pos[K] > max(pos[s:e]):
				 ans.append(pos[K])
		elif e == len(pos)-1:
			if pos[len(pos)-K-1] > max(pos[s:e]):
				ans.append(pos[len(pos)-K-1])
		else:
			if s > 0 and e < len(pos):
				if pos[s-1] > max(pos[s:e]) and pos[e] > max(pos[s:e]):
					ans.append(max(pos[s-1],pos[e]))
		s+= 1
		e+= 1
	if ans == []:
		return -1
	else:
		return max(ans)-1
print(solution([3,1,5,4,2], 1))