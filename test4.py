'''
Test4: 括号匹配

给定一个字符串，里边可能包含“()”、“[]”、“{}”三种括号，请编写程序检查该字符串中的括号是否成对出现，且嵌套关系正确。
输出：true:若括号成对出现且嵌套关系正确，或该字符串中无括号字符；
false:若未正确使用括号字符。
实现时，无需考虑非法输入。

输入描述：
输入为：
字符串
例子：(1+2)/(0.5+1)
输出描述：
输出为：
字符串
例子：true
'''
import sys


def isMatch(a):
    length = len(a)
    if a == []:
        return True
    elif not(a[0] in ["{", "[", "("]):
        return False
    else:
        if a[0] == "{":
            try:
                i = a.index("}")
            except Exception as e:
                return False
            else:
                if i == length-1:
                    return isMatch(a[1:i])
                else:
                    return isMatch(a[1:i]) and isMatch(a[i+1:])
        elif a[0] == "[":
            try:
                i = a.index("]")
            except Exception as e:
                return False
            else:
                if i == length-1:
                    return isMatch(a[1:i])
                else:
                    return isMatch(a[1:i]) and isMatch(a[i+1:])
        elif a[0] == "(":
            try:
                i = a.index(")")
            except Exception as e:
                return False
            else:
                if i == length-1:
                    return isMatch(a[1:i])
                else:
                    return isMatch(a[1:i]) and isMatch(a[i+1:])
        return True


lst = list(sys.stdin.readline().strip())
temp = []
for i in lst:
    if i in ["{", "[", "(", "}", "]", ")"]:
        temp.append(i)
print(isMatch(temp))
