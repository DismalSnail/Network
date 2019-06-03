"""
    将所有的数据整合到一个文件中
    数据：
    1.所有站点的坐标
    2.骨干路线

    3.骨干-聚类-中心性
    4.骨干-非聚类-中心性

    5.骨干-聚类-重要性
    6.骨干-非聚类-重要性
"""

import nodesort as ns
import edgesort as es

JsonFile = open("Json/ALLData.json", "w")
JsonFile.write("{\"station\":[")

a = [-1] * 418
flag = 0

# 输入将数据点写入文本
with open("Csv/LocationList.csv", "r") as NodeCsvFile:
    for row in NodeCsvFile:
        if flag == 0:
            flag = 1
            continue
        else:
            middle = row.strip('\n')
            middle = middle.split(',')
            a[int(middle[0])] = [middle[0], middle[1], middle[2]]

for i in range(len(a)):
    if a[i] == -1:
        a[i] = ['-1', '-1', '-1']
    if i == len(a) - 1:
        JsonFile.write('[' + a[i][0] + ',' + a[i][1] + ',' + a[i][2] + ']')
    else:
        JsonFile.write('[' + a[i][0] + ',' + a[i][1] + ',' + a[i][2] + '],')

# 将骨干路径写入文本
JsonFile.write("],\"SHH_routes\":[")
count = 0
with open("Csv/TrainSHH.csv", "r") as RouteCsvFile:
    RouteCsvFile.readline()
    row = RouteCsvFile.readline()
    while row:
        NextLine = RouteCsvFile.readline()
        if NextLine != "":
            middle = row.strip('\n')
            middle = middle.split(',')
            JsonFile.write('[' + middle[0] + ',' + middle[1] + '],')
            count = count + 1
        else:
            middle = row.strip('\n')
            middle = middle.split(',')
            JsonFile.write('[' + middle[0] + ',' + middle[1] + ']')
            count = count + 1
        row = NextLine

# 骨干-聚类-中心性
JsonFile.write("],\"cluster_centrality\":[")
node = ns.nodes_sort(0.5, cluster=True)
print(len(node))
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-非聚类-中心性
JsonFile.write("],\"centrality\":[")
node = ns.nodes_sort(0.5, cluster=False)
print(len(node))
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")

# 骨干-聚类-重要性
JsonFile.write("],\"cluster_salience\":[")
node = es.edges_sort(0.5, cluster=True)
node = list(node)
print(len(node))
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-非聚类-重要性
JsonFile.write("],\"salience\":[")
node = es.edges_sort(0.5, cluster=False)
node = list(node)
print(len(node))
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")

JsonFile.write("]}")
JsonFile.close()
