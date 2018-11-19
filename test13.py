'''
Test13:跳跃比赛
题目描述
给出一组正整数，你从第一个数向最后一个数方向跳跃，每次至少跳跃1格，每个数的值表示你从这个位置可以跳跃的最大长度。计算如何以最少的跳跃次数跳到最后一个数。

输入描述:
第一行表示有多少个数n
第二行开始依次是1到n个数，一个数一行
输出描述:
输出一行，表示最少跳跃的次数。
示例1
输入
7
2
3
2
1
2
1
5
输出
3
'''
num = int(input())
ls = []
for i in range(num):
    ls.append(int(input()))
step = 0
out = 0
step_max = 0
while(True):
    step += 1
    for i in range(out+1):
        if (ls[i]+i > step_max):
            step_max = ls[i]+i
    out = step_max
    if (out + 1 >= len(ls)):
        break

print(step)
