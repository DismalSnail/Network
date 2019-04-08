import csv

csvFile = open("CSV/trainnew.csv", "r")
csvSaveFile=open("CSV/trainweight.csv","w+",newline="")
csvreader = csv.reader(csvFile)
csvwriter=csv.writer(csvSaveFile)
flag = False

Graph = []

for item in csvreader:
    flag = False
    middleList = []
    if csvreader.line_num == 1:
        continue
    else:
        middleList.append(int(item[0]))
        middleList.append(int(item[1]))
        middleList.append(1)
        for edge in Graph:
            if middleList[0] == edge[0] and middleList[1] == edge[1]:
                edge[2] = edge[2] + middleList[2]
                flag = True
                break
        if not flag:
            Graph.append(middleList)

csvwriter.writerow(["source","target","weight"])

for line in Graph:
    csvwriter.writerow(line)

csvSaveFile.close()
csvFile.close()
