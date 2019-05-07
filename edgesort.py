"""
    按节点重要度缩减节点
"""
import csv
import networkx as nx
import dbscan as db

__all__ = ['edges_sort']


def take_third(elem):
    return elem[2].get('weight')


def edges_sort(percentage=0.5, cluster=False, sal=False):
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
    end_node_list = []
    end_num = []
    flag = True
    if cluster:  # 使用聚类
        db_list = db.db_scan()
        noise = db_list.pop()  # 噪声点保留
        for i in range(len(db_list)):  # 与聚类数组对应的数组
            end_node_list.append([])
            end_num.append(False)  # 每一个聚类达到要求的标志
        weight = list(g.edges(data=True))
        weight.sort(key=take_third, reverse=True)
        weight_iter = iter(weight)
        while True:
            try:
                line = weight_iter.__next__()  # 一条边
                start, end = line[0], line[1]
                for e_list in db_list:
                    index = db_list.index(e_list)  # 聚类簇所在的索引
                    init_node_num = len(e_list)  # 该聚类中元素的个数
                    end_node_num = len(set(end_node_list[index]))  # 存贮节点对应数组的元素个数
                    if end_node_num / init_node_num > percentage:
                        continue
                        end_num[index] = True
                    if start in e_list:
                        end_node_list[index].append(start)
                    if end in db_list:
                        end_node_list[index].append(end)
                for elem in end_num:
                    flag = flag and elem
                if flag:
                    break
            except StopIteration:
                break
        if flag:  # 所有聚类达到要求
            for elem in end_node_list:
                end_node.update(elem)
            end_node.update(noise)
            return end_node
        else:
            for e_list in db_list:
                index = db_list.index(e_list)
                init_node_num = len(e_list)
                end_node_num = len(set(end_node_list[index]))
                if end_num[index]:
                    continue
                else:
                    for elem in e_list:
                        while end_node_num / init_node_num < percentage:
                            end_node_list[index].append(elem)
                            end_node_num = len(set(end_node_list[index]))
            for elem in end_node_list:
                end_node.update(elem)
            end_node.update(noise)
            return end_node

    else:  # 不使用聚类
        weight = list(g.edges(data=True))
        weight.sort(key=take_third, reverse=True)
        init_node_num = len(g.nodes())
        end_node_num = 0
        weight_iter = iter(weight)
        while end_node_num / init_node_num < percentage:
            try:
                line = weight_iter.__next__()
                end_node.update([line[0], line[1]])
                end_node_num = len(end_node)
            except StopIteration:
                break
        return end_node


if __name__ == "__main__":
    node = edges_sort(0.5, cluster=True, sal=True)
    print(len(node))
    for s in node:
        print(s)
