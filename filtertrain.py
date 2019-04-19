"""
    初始路线中的部分端点在站点数据中没有
    因此剔除端点数据不存在的路线
"""
import csv

csvFile=open("Csv/LocationList.csv","r")
csvRe=open("Csv/OnlyTrain.csv","r")
csvSv=open("Csv/FilterTrain.csv","w",newline='')
reader=csv.reader(csvFile)
reade=csv.reader(csvRe)
writer=csv.writer(csvSv)
result=[]
for item in reader:
    if reader.line_num==1:
        continue
    result.append(int(item[0]))

for str in reade:
    if reade.line_num==1:
        writer.writerow(str)
    else:
        if int(str[0]) in result and int(str[1]) in result:
            writer.writerow(str)


for j in result:
    print(j)


csvFile.close()
csvRe.close()
csvSv.close()

