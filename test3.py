'''
Test3：长整数相乘
import sys
for line in sys.stdin:
    list = line.split()
    num1 = int(list[0])
    num2 = int(list[1])
    print(num1*num2)


Test3_extension: 长整数相乘
输入描述:
输入两个长整数，以空格隔开
输出描述:
输出相乘后的结果

示例1
输入
-12341234
43214321
输出
-533318047612114
'''
import sys
num1 = int(sys.stdin.readline().strip())
num2 = list(sys.stdin.readline().strip())
result = 0
neg = False

if num2[0] == "-":
    num2.pop()
    neg = True

for i in range(0, len(num2)):
    temp = int(num2[i] + "0" * (len(num2) - 1 - i))
    # print("temp: {}".format(temp))
    result += temp * num1
    # print("result: {}".format(result))

if neg:
    result *= -1
print(result)
