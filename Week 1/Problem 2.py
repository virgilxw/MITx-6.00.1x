count = 0
n = 0

for n in range(len(s)):
    if (s[n:n+3]) == "bob":
        count += 1

print ("Number of times bob occurs is: " + str(count))