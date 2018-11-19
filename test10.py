'''
Test10:
两个字符串input1和input2，判断input2中所有字符是否包含在字符串input1中
例如：

输入：
BBDDCFFEL
LCEFB

输出：
True
'''
import sys


def isAllIn(a, b):
    for char in b:
        try:
            a.index(char)
        except Exception as e:
            return False
        else:
            pass
    return True


input1 = list(sys.stdin.readline().strip())
input2 = list(sys.stdin.readline().strip())
print(isAllIn(input1, input2))
