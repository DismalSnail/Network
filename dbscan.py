import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from math import radians, sin, cos, asin, sqrt
import csv

__all__ = ['db_scan']


def haversine(latlon1, latlon2):
    """
    计算两经纬度之间的距离
    """
    if (latlon1 - latlon2).all():
        lat1, lon1 = latlon1
        lat2, lon2 = latlon2
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 6370996.81  # 地球半径
        distance = c * r
    else:
        distance = 0
    return distance


def db_scan(min_pts=3, eps=650):
    datap = []
    f = open("Csv/LocationList.csv", 'r')
    reader = csv.reader(f)
    for line in reader:
        if reader.line_num == 1:
            continue
        else:
            datap.append([int(line[0]), float(line[1]), float(line[2])])
    num_data = datap
    data_s = [[elem[1], elem[2]] for elem in datap]
    data = np.array(data_s)

    db = DBSCAN(eps=eps, min_samples=min_pts, metric=haversine).fit(data)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    s = db.labels_[db.labels_ == -1]
    s = s.tolist()
    unique_labels = set(labels)
    label_list = []
    for k in unique_labels:
        class_member_mask = (labels == k)
        middle = []
        for elem in data[class_member_mask]:
            mid_list = elem.tolist()
            index = data_s.index(mid_list)
            middle.append(num_data[index][0])
        label_list.append(middle)

    return label_list


if __name__ == "__main__":
    data = []
    f = open("Csv/LocationList.csv", 'r')
    reader = csv.reader(f)
    for line in reader:
        if reader.line_num == 1:
            continue
        else:
            data.append([float(line[1]), float(line[2])])
    data = np.array(data)
    MinPts = 3
    eps = 650

    db = DBSCAN(eps=eps, min_samples=MinPts, metric=haversine).fit(data)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    unique_labels = set(labels)
    # colors = ['r', 'b', 'g', 'y', 'c', 'm', 'orange']
    c_map = plt.get_cmap('hsv')
    colors = [c_map(i) for i in np.linspace(0.2, 0.8, n_clusters_ + 1)]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = '#000000'
        class_member_mask = (labels == k)
        xy = data[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=10)

        xy = data[class_member_mask & ~core_samples_mask]
        if k == -1:
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=10)
        else:
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=3)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()
