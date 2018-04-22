def isIn(str1, str2):
    if (str1 in str2) or (str2 in str1):
        return True
    else:
        return False

print(isIn('1', '2'))
print(isIn('12', '2'))
print(isIn("12111", '21'))
print(isIn('212', '12'))
