'''
Test7: 输入任意个字符串，将其中的小写字母变为大写，大写字母变为小写，其他字符不用处理

输入描述：abcd12#%XYZ

输出描述：ABCD12#%xyz
'''
import sys

strList = list(sys.stdin.readline().strip())
temp = []
for char in strList:
    if char.isalpha():
        if char.islower():
            temp.append(char.upper())
        else:
            temp.append(char.lower())
    else:
        temp.append(char)
# print(*temp, sep='')
print(''.join(temp))
