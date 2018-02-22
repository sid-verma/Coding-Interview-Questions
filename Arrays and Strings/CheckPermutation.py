# Solution 1: [SUB-OPTIMAL]
# Key Step: Sort the Arrays and Compare them
# TC: O(n lgn)
# SC: O(1)

def isPermutation1(a, b):
	if len(a) != len(b):
		return False

	a , b = sorted(a), sorted(b)
	return a == b

# Solution 2:
# Key Step: Store character counts in HashMap
# TC: O(n + m) where n and m are the lengths of the two strings
# SC: O(n + m)

def isPermutation2(a, b):
	if len(a) != len(b):
		return False

	charMap = {}
	for i in a:
		if i not in charMap:
			charMap[i] = 1
		else:
			charMap[i] += 1
	for j in b:
		charMap[j] -= 1
		if charMap[j] < 0:
			return False
	return True

def main():
	print(isPermutation1('abcdd', 'ddcba'))
	print(isPermutation2('vbfres', 'bfersv'))

if __name__ == '__main__':
	main()
