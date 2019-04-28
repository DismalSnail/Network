"""
    按节点重要度缩减节点
"""
import csv
import networkx as nx
import dbscan as db


def take_second(elem):
    return elem[1]


def nodes_sort(percentage=0.5, cluster=False, sal=False):
    """返回删减后的节点

    :param percentage: 保留节点百分比
    :param cluster: 是否聚类，默认不使用
    :param sal: 是否使用高显著性骨架，默认不使用
    :return: 删减后节点列表
    """
    if sal:
        with open("Csv/TrainSHH.csv", "r") as reader:
            reader.readline()
            csv_reader = csv.reader(reader)
            edges = [tuple([int(item[0]), int(item[1])]) for item in csv_reader]
    else:
        with open("Csv/TrainWeight.csv", "r") as reader:
            reader.readline()
            csv_reader = csv.reader(reader)
            edges = [tuple([int(item[0]), int(item[1])]) for item in csv_reader]

    with open("Csv/LocationList.csv", "r") as reader:
        reader.readline()
        csv_reader = csv.reader(reader)
        nodes = [int(item[0]) for item in csv_reader]

    g = nx.Graph()
    g.add_edges_from(edges)
    g.add_nodes_from(nodes)
    end_node = []
    if cluster:
        db_list = db.db_scan()
        noise = db_list.pop()
        for e_list in db_list:
            degree = [(n, g.degree(n)) for n in e_list]
            init_node_num = len(degree)
            end_node_num = len(degree)
            degree.sort(key=take_second, reverse=True)
            if end_node_num == 1:
                end_node = end_node + degree
                continue
            while end_node_num / init_node_num > percentage:
                degree.pop()
                end_node_num = len(degree)
                if end_node_num == 1:
                    break
            end_node = end_node + degree
        return [elem[0] for elem in end_node] + noise
    else:
        degree = list(g.degree())
        init_node_num = len(degree)
        end_node_num = len(degree)
        degree.sort(key=take_second, reverse=True)
        while end_node_num / init_node_num > percentage:
            degree.pop()
            end_node_num = len(degree)
        end_node = [elem[0] for elem in degree]
        return end_node


if __name__ == "__main__":
    node = nodes_sort(0.5, cluster=True, sal=True)
    print(len(node))
