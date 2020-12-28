def addNumString(str1, str2):
    if len(str1) == 0:
        str1 = 0
    if len(str2) == 0:
        str1 = 0
    return str(int(str1) + int(str2))


print(addNumString("2", "7"))
