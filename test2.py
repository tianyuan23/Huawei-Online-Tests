'''
Test2: 字节流解析
根据数值占用BIT数，按顺序从输入字节流中解析出对应数值，解析顺序按输入数组astElement索引升序；
void Decode(unsigned int uiInputLen, unsigned char aInputByte[], unsigned int uiElementNum, ELEMENT_STRU astElement[]);
unsigned int uiInputLen：字节数组（流）长度
unsigned char aInputByte：字节数组（流）
unsigned int uiElementNum：解析数值个数
ELEMENT_STRU astElement[]：数值的结构数组指针，含义如下
Struct
{
unsigned int uiElementLength; //表示uiElementValue占用BIT数，范围1~32
unsigned int uiElementValue; //从字节流中按顺序解析的数值，用于输出
}ELEMENT_STRU;

输入描述:
字节数组长度uiIutputLen为3；
字节数组aInputByte[3]为{0x62, 0x80, 0x00}，对应二进制为“0110 0010, 1000 0000, 0000 0000”；
解析数值个数uiElementNum为2；
数值[0]的值占4个bit，即astElement[0].uiElementLength = 4；
数值[1]的值占5个bit，即astElement[1].uiElementLength = 5；
输出描述:
数值[0]的值为6，二进制为“0110”，即astElement[0].uiElementValue = 6；
数值[1]的值为5，二进制为“0010 1”，即astElement[1].uiElementValue = 5；
'''
import sys
uiIutputLen = int(sys.stdin.readline().strip())
aInputByte = sys.stdin.readline().strip().split(',')
binSeq = ""
for seq in aInputByte:
    binSeq += bin(int(seq[2:], 16))[2:].zfill(len(seq[2:])*4)
uiElementNum = int(sys.stdin.readline().strip())
result = []
for i in range(0, uiElementNum):
    bitNum = int(sys.stdin.readline().strip())
    result.append(int(binSeq[0:bitNum], 2))
    binSeq = binSeq[bitNum:]
for i in result:
    print(i)
