# Key Step: Add extra length to the array based on initial length + 2 * no. of spaces.
#			Start index from reverse of array, but start writing from new length in reverse.
#			If you encounter space, add '%20' in reverse, and skip 3 counts.
#			If you encounter non-sapce add the character and skip 1 count.
# TC: O(n)
# SC: O(1) In place

def URLify(s):
	for i in reversed(s):


def newLen(s):
	spaceCount = 0
	for i in s:
		if i == ' ':
			spaceCount += 1
	return len(s) + 2 * spaceCount

