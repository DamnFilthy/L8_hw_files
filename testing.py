str1 = 'AAAAAAAAAAAA'
result = []
try:
    for i in range(len(str1)):
        if str1[i] == str1[i+1] and str1[i] != str1[i+2]:
            result.append(str1[i])
        elif str1[i] != str1[i-1] and str1[i] != str1[i+1]:
            result.append(str1[i])
except IndexError:
    result.append(str1[i])
