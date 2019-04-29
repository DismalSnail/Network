"""
    按节点重要度缩减节点
"""
import csv
import networkx as nx
import dbscan as db


def take_third(elem):
    return elem[2].get('weight')


def edges_sort(percentage=0.5, cluster=False, sal=False, ipt_is=0):
    """返回删减后的节点

    :param percentage: 保留节点百分比
    :param cluster: 是否聚类，默认不使用
    :param sal: 是否使用高显著性骨架，默认不使用
    :param ipt_is: 边重要度计算方法 0：权重 1：边介数
    :return: 删减后节点列表
    """
    if sal:  # 骨架网络
        with open("Csv/TrainSHH.csv", "r") as reader:
            reader.readline()
            csv_reader = csv.reader(reader)
            edges = [tuple([int(item[0]), int(item[1]), float(item[2])]) for item in csv_reader]
    else:  # 非骨架网络
        with open("Csv/TrainWeight.csv", "r") as reader:
            reader.readline()
            csv_reader = csv.reader(reader)
            edges = [tuple([int(item[0]), int(item[1]), int(item[2])]) for item in csv_reader]

    with open("Csv/LocationList.csv", "r") as reader:  # 节点信息
        reader.readline()
        csv_reader = csv.reader(reader)
        nodes = [int(item[0]) for item in csv_reader]

    g = nx.Graph()
    g.add_weighted_edges_from(edges)
    g.add_nodes_from(nodes)
    end_node = set()  # 存储缩减后的节点
    if cluster:  # 使用聚类
        db_list = db.db_scan()
        noise = db_list.pop()  # 噪声点保留
        for e_list in db_list:  # 将每一个聚类进行缩减
            if ipt_is == 0:  # 节点度
                degree = [(n, g.degree(n)) for n in e_list]
            else:  # 特征向量中心性
                centrality = nx.eigenvector_centrality(g)
                degree = [(n, centrality.get(n)) for n in e_list]
            init_node_num = len(degree)
            end_node_num = len(degree)
            degree.sort(key=take_third, reverse=True)
            while end_node_num / init_node_num > percentage:
                degree.pop()
                end_node_num = len(degree)
                if end_node_num == 1:  # 只有一个节点的聚类保留
                    break
            end_node = end_node + degree
        return [elem[0] for elem in end_node] + noise
    else:  # 不使用聚类
        if ipt_is == 0:  # 边权重
            weight = list(g.edges(data=True))
            weight.sort(key=take_third, reverse=True)
        else:  # 边介数
            pass
        init_node_num = len(g.nodes())
        end_node_num = 0
        weight_iter = iter(weight)
        while end_node_num / init_node_num < percentage:
            line = weight_iter.__next__()
            end_node.update([line[0], line[1]])
            end_node_num=len(end_node)
        return end_node


if __name__ == "__main__":
    node = edges_sort(0.5, cluster=False, sal=False, ipt_is=0)
    print(len(node))
    for s in node:
        print(s)
