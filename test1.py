'''
Test1: 最长数字字符串
给定一个字符串，输出字符串中最长的数字串，并把这个数字串的长度输出。

请一个在字符串中找出连续最长的数字串，并把这个串的长度返回；如果存在长度相同的连续数字串，返回最后一个连续数字串；

注意：数字串只需要是数字组成的就可以，并不要求顺序，比如数字串“1234”的长度就小于数字串“1359055”，如果没有数字，则返回空字符串（“”）而不是NULL！

输入描述:
一个字符串
输出描述:
输出最长的数字串,输出最长数字串个数；
中间以逗号(,)隔开；

示例1
输入
abcd12345ed125ss123058789
输出
123058789,9

备注:
1、如果存在长度相同的连续数字串，则输出最后一个连续数字串；
2、数字串只需要是数字组成的就可以，并不要求顺序，比如数字串“1234”的长度就小于数字串“1359055”；
3、如果没有数字，则输出空字符串（“”）而不是NULL；
'''
import sys

inputList = list(sys.stdin.readline().strip())
max = ""
temp = ""
for i in range(0, len(inputList)):
    if inputList[i].isdigit():
        temp += inputList[i]
        # print(temp)
    else:
        if len(temp) >= len(max):
            max = temp
        temp = ""
if len(temp) >= len(max):
    max = temp
print("{},{}".format(max, len(max)))
