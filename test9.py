'''
Test9:
第一题 求26进制的和
给出两个26进制的数，求和
input:
z
bc
output:
cb
'''
import sys
import string

a = list(sys.stdin.readline().strip())
a.reverse()
b = list(sys.stdin.readline().strip())
b.reverse()
ls = list(string.ascii_lowercase)
temp1 = 0
temp2 = 0
for i in range(len(a)):
    temp1 += 26 ** i * ls.index(a[i])

for i in range(len(b)):
    temp2 += 26 ** i * ls.index(b[i])

result = temp1 + temp2

temp3 = []

while(result != 0):
    temp3.append(ls[int(result % 26)])
    result = int(result / 26)

temp3.reverse()
print(''.join(temp3))
