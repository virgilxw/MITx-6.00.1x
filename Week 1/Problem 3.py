#currentString = longestString = s[0]
#
#for sPointer in range(1, len(s)):
#    if s[sPointer] >= currentString[-1]:
#        currentString += s[sPointer]
#        print(currentString, len(currentString))
#    
#        if len(currentString) > len(longestString):
#            longestString = currentString
#    else:
#        currentString = str(s[sPointer])

longestIndex = 0
longestLength = 0
            
for n in range(len(s)):
    if n == 0:
        tempIndex = n
        tempLength = 1
    elif s[n] > s[n-1]:
        tempLength += 1
        if tempLength > longestLength:
            longestLength = tempLength
        else:
            tempIndex = n
            tempLength = 1

if tempLength > longestLength:
            longestLength = tempLength
            longestIndex = tempIndex
print ("Longest substring in alphabetical order is:", s[longestIndex:longestIndex+longestLength])