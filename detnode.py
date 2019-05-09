"""
    将所有的数据整合到一个文件中
    数据：
    1.所有站点的坐标
    2.权重路线
    3.骨干路线

    4.非骨干-聚类-度
    5.非骨干-聚类-中心性
    6.非骨干-非聚类-度
    7.非骨干-非聚类-中心性
    8.骨干-聚类-度
    9.骨干-聚类-中心性
    10.骨干-非聚类-度
    11.骨干-非聚类-中心性

    12.非骨干-聚类-权重
    13.非骨干-非聚类-权重
    14.骨干-聚类-重要性
    15.骨干-非聚类-重要性
"""

import nodesort as ns
import edgesort as es

JsonFile = open("Json/AllData.json", "w")
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

JsonFile.write("],\"weight_routes\":[")

# 将权重路线写入文本
count = 0
with open("Csv/TrainWeight.csv", "r") as RouteCsvFile:
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

# 将重要度路径写入文本
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

# 非骨干-聚类-度
JsonFile.write("],\"cluster_degree\":[")
node = ns.nodes_sort(0.5, cluster=True, sal=False, ipt_is=0)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 非骨干-聚类-中心性
JsonFile.write("],\"cluster_centrality\":[")
node = ns.nodes_sort(0.5, cluster=True, sal=False, ipt_is=1)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 非骨干-非聚类-度
JsonFile.write("],\"degree\":[")
node = ns.nodes_sort(0.5, cluster=False, sal=False, ipt_is=0)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 非骨干-非聚类-中心性
JsonFile.write("],\"centrality\":[")
node = ns.nodes_sort(0.5, cluster=False, sal=False, ipt_is=1)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-聚类-度
JsonFile.write("],\"SHH_cluster_degree\":[")
node = ns.nodes_sort(0.5, cluster=True, sal=True, ipt_is=0)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-聚类-中心性
JsonFile.write("],\"SHH_cluster_centrality\":[")
node = ns.nodes_sort(0.5, cluster=True, sal=True, ipt_is=1)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-非聚类-度
JsonFile.write("],\"SHH_degree\":[")
node = ns.nodes_sort(0.5, cluster=False, sal=True, ipt_is=0)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-非聚类-中心性
JsonFile.write("],\"SHH_centrality\":[")
node = ns.nodes_sort(0.5, cluster=False, sal=True, ipt_is=1)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 非骨干-聚类-权重
JsonFile.write("],\"weight_cluster\":[")
node = es.edges_sort(0.5, cluster=True, sal=False)
node = list(node)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 非骨干-非聚类-权重
JsonFile.write("],\"weight\":[")
node = es.edges_sort(0.5, cluster=False, sal=False)
node = list(node)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-聚类-重要性
JsonFile.write("],\"SHH_cluster_salience\":[")
node = es.edges_sort(0.5, cluster=True, sal=True)
node = list(node)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")
# 骨干-非聚类-重要性
JsonFile.write("],\"salience\":[")
node = es.edges_sort(0.5, cluster=False, sal=False)
node = list(node)
for i in range(len(node)):
    if i == len(node) - 1:
        JsonFile.write(str(node[i]))
    else:
        JsonFile.write(str(node[i]) + ",")

JsonFile.write("]}")
JsonFile.close()
