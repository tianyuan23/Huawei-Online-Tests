str = list(input())
d = {}
key = ""
value = ""
for i in range(len(str)):
    if str[i].isalpha() and (key == "" or value == ""):
        key += str[i]
    elif str[i].isdigit() and (i != len(str) - 1):
        value += str[i]
    elif str[i].isalpha() and value != "":
        d[key] = int(value)
        key = "" + str[i]
        value = ""
    elif str[i].isdigit() and (i == len(str) - 1):
        value += str[i]
        d[key] = int(value)
        key = ""
        value = ""
print(d)

# a11b2bac3bad3abcd2
result = ""
while len(d.values()) != 0:
    minFreq = min(d.values())
    temp = []
    for key, value in d.items():
        if value == minFreq:
            temp.append(key)
    temp = min(temp)
    result += temp * d[temp]
    del d[temp]
print(result)
