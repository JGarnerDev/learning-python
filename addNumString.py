# Given two number-strings, return the sum as a string
# If the string is empty, convert it to "0"

#   Solution 1:

def addNumString(str1, str2):
    if len(str1) == 0:
        str1 = 0
    if len(str2) == 0:
        str1 = 0
    return str(int(str1) + int(str2))


print(addNumString("2", "7"))

#   Solution 2:

def addNumString2(*values):
    return str(sum(int(v or 0) for v in values))

print(addNumString2("", "8"))
print(addNumString2("2", "8"))