import networkx as nx
import salience as sa
import csv

csvFile = open("CSV/trainweight.csv", "r")
csvreader = csv.reader(csvFile)

edgeList = []

for item in csvreader:
    middlelist = []
    if csvreader.line_num == 1:
        continue
    else:
        middlelist.append(int(item[0]))
        middlelist.append(int(item[1]))
        middlelist.append(int(item[2]))
        edgeList.append(tuple(middlelist))

for item in edgeList:
    print(item)

G = nx.Graph()
G.add_weighted_edges_from(edgeList)
print(G.number_of_edges())

csvFile.close()
