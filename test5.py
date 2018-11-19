'''
Test5:打印机任务
简要描述：
某个打印机根据打印机队列执行打印任务，打印任务分为九个优先级，分别用数字1~9表示，数字越大优先级越高。打印机每次从队列头部取出第一个任务A，然后检查队列余下任务中有没有比A优先级更高的任务，则将任务A放在队列尾部，否则就执行任务A的打印。请编写一个程序，根据输入的打印队列，编出实际的打印顺序。
输入描述：
函数原型： void printOrder(const int input[], int len, int output[])
输入参数input表示打印队列，为一个由整数1~9（优先级）组成的数组，数组索引0表示打印队列头部。对于C/C++,参数len表示input数组的长度。可以假定输入的参数总是合法有效的，input数组长度有可能为0，但不会是空指针。
输出为一个表示实际打印顺序的数组，其数组项为打印任务在输入数组中的索引值（从0开始）。Java通过返回值输出。C/C++通过输出参数output[]输出，可以假定为存放结果分配了足够的空间
。。。。题目其余部分没有记录，有人记录的，可以希望在留言处补全，大家一起分享交流。
输入样例：
9, 3, 5
输出样例：
0, 2, 1
'''
printList = input().split(",")
orderList = [0] * len(printList)
tempList = printList.copy()
i = 0
while tempList != []:
    length = len(tempList)
    temp = tempList[0]
    tempList.remove(temp)

    for j in range(0, len(tempList)):
        if int(temp) < int(tempList[j]):
            tempList.append(temp)
            break
    if len(tempList) != length:
        orderList[printList.index(temp)] = i
        i += 1
        printList[printList.index(temp)] = 0
print(*orderList, sep=",")
