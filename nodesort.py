"""
    按节点重要度缩减节点
"""
import csv
import networkx as nx
import dbscan as db

__all__ = ['nodes_sort']


def take_second(elem):
    return elem[1]


def nodes_sort(percentage=0.5, cluster=False):
    """返回删减后的节点

    :param percentage: 保留节点百分比
    :param cluster: 是否聚类，默认不使用
    :return: 删减后节点列表
    """

    with open("Csv/TrainSHH.csv", "r") as reader:
        reader.readline()
        csv_reader = csv.reader(reader)
        edges = [tuple([int(item[0]), int(item[1])]) for item in csv_reader]

    with open("Csv/LocationList.csv", "r") as reader:  # 节点信息
        reader.readline()
        csv_reader = csv.reader(reader)
        nodes = [int(item[0]) for item in csv_reader]

    g = nx.Graph()
    g.add_edges_from(edges)
    g.add_nodes_from(nodes)
    end_node = []  # 存储缩减后的节点
    centrality = nx.eigenvector_centrality(g)
    allc=0.0
    pc=0.0
    for v,c in centrality.items():
        allc=allc+c
    if cluster:  # 使用聚类
        db_list = db.db_scan()
        noise = db_list.pop()  # 噪声点保留
        for e_list in db_list:  # 将每一个聚类进行缩减
            degree = [(n, centrality.get(n)) for n in e_list]
            init_node_num = len(degree)
            end_node_num = len(degree)
            degree.sort(key=take_second, reverse=True)
            while end_node_num / init_node_num > percentage:
                degree.pop()
                end_node_num = len(degree)
                if end_node_num == 1:  # 只有一个节点的聚类保留
                    break
            end_node = end_node + degree
        for elem in end_node:
             pc=elem[1]+pc
        for elem in [centrality.get(n) for n in noise]:
            pc=pc+elem
        print("点-聚类 重要度保留比例："+str(pc/allc))
        return [elem[0] for elem in end_node] + noise
    else:  # 不使用聚类
        degree = [(v, value) for v, value in centrality.items()]
        init_node_num = len(degree)
        end_node_num = len(degree)
        degree.sort(key=take_second, reverse=True)
        while end_node_num / init_node_num > percentage:
            degree.pop()
            end_node_num = len(degree)
        end_node = [elem[0] for elem in degree]
        for elem in [centrality.get(n) for n in end_node]:
            pc=pc+elem
        print("点-无聚类 重要度保留比例："+str(pc/allc))
        return end_node
