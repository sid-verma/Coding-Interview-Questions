# Key Step: If the string is ASCII, use a Character Map of size 128 to store frequency
# TC: O(n) or O(1) since 128 is a fixed limit on iteratin
# SC: O(1)

def isUniqueChars(str):
    if len(str) > 128:
        return False
    charSet = {}
    for i in str:
        if i in charSet:
            return False
        charSet[i] = True
    return True

if __name__ == '__main__':
    inputString = 'vsrekjwbg'
    print "Result for ", inputString, "is", isUniqueChars(inputString)

# We can also replace the 128 size with a single bit vector [0,0,0,1,0,1,0,1] to store values
