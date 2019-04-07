import csv

csvFile=open("locationList.csv","r")
csvRe=open("train.csv","r")
csvSv=open("trainnew.csv","w+",newline='')
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
            #print(str[0]+','+str[1])


for j in result:
    print(j)


csvFile.close()
csvRe.close()
csvSv.close()

