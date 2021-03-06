'''
Test6: 平安果

简要描述：
给定一个M行N列的矩阵（M*N个格子），每个格子中放着一定数量的平安果。
你从左上角的各自开始，只能向下或者向右走，目的地是右下角的格子。
每走过一个格子，就把格子上的平安果都收集起来。求你最多能收集到多少平安果。
注意：当经过一个格子时，需要一次性把格子里的平安果都拿走。
限制条件：1<N,M<=50；每个格子里的平安果数量是0到1000（包含0和1000）.
输入描述：
输入包含两部分：
第一行M, N
接下来M行，包含N个平安果数量
输出描述：
一个整数
最多拿走的平安果的数量
示例：
输入
2 4
1 2 3 40
6 7 8 90
输出
136
'''
import sys

lst = sys.stdin.readline().strip().split()
rowNum, colNum = int(lst[0]), int(lst[1])
matrix = [0]*rowNum
for i in range(0, rowNum):
    matrix[i] = sys.stdin.readline().strip().split()

sumMatrix = matrix.copy()
sumMatrix[0][0] = int(matrix[0][0])

for i in range(1, rowNum):
    sumMatrix[i][0] = int(matrix[i][0]) + sumMatrix[i-1][0]

for i in range(1, colNum):
    sumMatrix[0][i] = int(matrix[0][i]) + sumMatrix[0][i-1]

for i in range(1, rowNum):
    for j in range(1, colNum):
        sumMatrix[i][j] = max(sumMatrix[i][j-1], sumMatrix[i-1][j])+int(matrix[i][j])
# print(sumMatrix)
print(sumMatrix[rowNum-1][colNum-1])
