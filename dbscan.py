import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from math import radians, sin, cos, asin, sqrt


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


if __name__ == "__main__":
    data = []
    f = open("TXT/Location1.txt", 'r')
    for line in f:
        data.append([float(line.split(',')[1]), float(line.split(',')[2])])
    data = np.array(data)
    MinPts = int(data.shape[0] / 100)
    eps = 500

    db = DBSCAN(eps=eps, min_samples=MinPts, metric=haversine).fit(data)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

    unique_labels = set(labels)
    # colors = ['r', 'b', 'g', 'y', 'c', 'm', 'orange']
    cmap = plt.get_cmap('gnuplot')
    colors = [cmap(i) for i in np.linspace(0.2, 0.8, n_clusters_)]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            col = '#000000'
        class_member_mask = (labels == k)
        xy = data[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=10)

        xy = data[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col, markeredgecolor='w', markersize=3)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()
