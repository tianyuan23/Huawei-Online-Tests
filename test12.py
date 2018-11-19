'''
Test12:字符串重排
题目描述
给你一个原始字符串，根据该字符串内每个字符出现的次数，按照ASCII码递增顺序重新调整输出。

【温馨提示】
(1).原始字符串中仅可能出现“数字”和“字母”；
(2).请注意区分字母大小写。

输入描述:
eeefgghhh
输出描述:
efghegheh

示例1
输入
eeefgghhh
输出
efghegheh
'''
ls = list(input())
result = ""
templst = []
while ls != []:
    result += min(ls)
    temp = min(ls)
    ls.remove(min(ls))
    print(ls)
    while len(ls) != 0 and temp < max(ls):
        for i in ls:
            if i > temp:
                templst.append(i)
        temp = min(templst)
        result += temp
        ls.remove(temp)
        templst = []
print(result)
