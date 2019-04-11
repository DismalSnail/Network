# 站点数据整理
# import csv
# import json
#
# csvfile=open('locationList.csv','r')
# sonfile=open('location.txt','w+')
#
# str=[]
# str2=[-1]
# a=[-1]*418
# flag=0
# for row in csvfile:
#     if flag==0:
#         flag=1;
#         continue
#     else:
#         str=row.strip('\n')
#         str=str.split(',')
#         str2[0]=int(str[0])
#         a[str2[0]]=[str[0],str[1],str[2]]
#
# for i in range(len(a)):
#     if a[i]==-1:
#         a[i]=['-1','-1','-1']
#
# sonfile.write('[')
#
# for row in a:
#     sonfile.write('[' + row[0]+','+row[1]+','+row[2]+']'+',')
#
# csvfile.close()
# sonfile.close()

# 数据路线整理
import csv
import json

csvfile=open('CSV/trainweight1.csv','r')
sonfile=open('TXT/routes.txt','w+')
sonfile.write('[')
str=[]
str2=[-1]
a=[]
flag=0
for row in csvfile:
    if flag==0:
        flag=1
        continue
    else:
        str=row.strip('\n')
        str=str.split(',')
        sonfile.write('['+str[0]+','+str[1]+','+str[2]+'],')

sonfile.write(']')

csvfile.close()
sonfile.close()
