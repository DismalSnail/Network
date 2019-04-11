import networkx as nx
import salience as sa
import csv

csvFile = open("CSV/trainweight.csv", "r")  # 读取文件
csvreader = csv.reader(csvFile)

edgeList = []  # 存储边的list

for item in csvreader:
    middlelist = []
    if csvreader.line_num == 1:
        continue
    else:
        middlelist.append(int(item[0]))
        middlelist.append(int(item[1]))
        middlelist.append(int(item[2]))
        edgeList.append(tuple(middlelist))

csvFile.close()

# for item in edgeList:
#     print(item)

G = nx.Graph()
G.add_weighted_edges_from(edgeList)
print(G.number_of_edges())
print(G.number_of_nodes())
nodeList = list(G.nodes())

edgeIndexList = []

for item in edgeList:
    edgeIndexList.append(tuple([nodeList.index(item[0]), nodeList.index(item[1]), item[2]]))

# for item in edgeIndexList:
#     print(item)

H = nx.Graph()
H.add_weighted_edges_from(edgeIndexList)
Salience = sa.salience(H, 'weight')

print(type(Salience))

# [rows, cols] = Salience.shape
#
# edgeList = []
#
# for i in range(rows):
#     for j in range(cols):
#         edgeList.append(tuple([nodeList[i], nodeList[j], Salience[i][j]]))
#
# G = nx.Graph()
#G.add_weighted_edges_from(edgeList)