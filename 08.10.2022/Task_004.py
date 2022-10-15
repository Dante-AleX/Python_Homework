# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data1 = open('file_with_data.txt', 'r')
myData = []
for line in data1:
    myData.extend(line)
data1.close()
count = 1
myNewData = []
for index in range(1, len(myData)):
    if myData[index-1] == myData[index] and index != len(myData)-1:
        count += 1
    elif myData[index-1] != myData[index] and index != len(myData)-1:
        myNewData.append(count)
        myNewData.append(myData[index-1])
        count = 1
    elif index == len(myData)-1:
        count += 1
        myNewData.append(count)
        myNewData.append(myData[index])
with open('file_with_newdata.txt', 'w') as data2:
    data2.write(''.join(map(str, myNewData)))
