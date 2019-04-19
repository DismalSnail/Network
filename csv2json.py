

"""
    将站点数据与路线数据整合转化为json数据
"""

JsonFile = open("Json/FilterTrainData.json", "w")
JsonFile.write("{\"station\":[")

a = [-1] * 418
flag = 0

# 输入将数据点写入文本
with open("CSV/LocationList.csv", "r") as NodeCsvFile:
    for row in NodeCsvFile:
        if flag == 0:
            flag = 1
            continue
        else:
            str = row.strip('\n')
            str = str.split(',')
            a[int(str[0])] = [str[0], str[1], str[2]]

for i in range(len(a)):
    if a[i] == -1:
        a[i] = ['-1', '-1', '-1']
    if i == len(a)-1:
        JsonFile.write('[' + a[i][0] + ',' + a[i][1] + ',' + a[i][2] + ']')
    else:
        JsonFile.write('[' + a[i][0] + ',' + a[i][1] + ',' + a[i][2] + '],')

JsonFile.write("],\"routes\":[")

# 将路线写入文本
count=0
with open("CSV/FilterTrain.csv", "r") as RouteCsvFile:
    RouteCsvFile.readline()
    row = RouteCsvFile.readline()
    while row:
        NextLine = RouteCsvFile.readline()
        if NextLine != "":
            str = row.strip('\n')
            str = str.split(',')
            JsonFile.write('[' + str[0] + ',' + str[1] + '],')
            count = count + 1
        else:
            str = row.strip('\n')
            str = str.split(',')
            JsonFile.write('[' + str[0] + ',' + str[1] + ']')
            count = count + 1
        row = NextLine

JsonFile.write("]}")
JsonFile.close()
