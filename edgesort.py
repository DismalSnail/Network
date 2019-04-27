"""
    按边重要度缩减节点
"""
import csv
import networkx as nx


def edges_sort(percentage=0.5, cluster=False):
    """返回删减后的节点

    :param percentage: 删减节点百分比
    :param cluster: 是否聚类，默认不使用
    :return: 删减后节点列表
    """
    with open("Csv/TrainWeight.csv", "r") as reader:
        reader.readline()
        csv_reader = csv.reader(reader)
        edges = [tuple([int(item[0]), int(item[1]), int(item[2])]) for item in csv_reader]

    with open("Csv/LocationList.csv", "r") as reader:
        reader.readline()
        csv_reader = csv.reader(reader)
        nodes = [int(item[0]) for item in csv_reader]

    g = nx.Graph()
    g.add_weighted_edges_from(edges)
    g.add_nodes_from(nodes)

    if cluster:
        pass
    else:
        pass


