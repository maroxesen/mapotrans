#!/usr/bin/env python2
import json
from sklearn.cluster import MeanShift, estimate_bandwidth
from numpy import array, unique

pred = lambda geo: geo['geometry']['type'] == u'LineString'

def make(filename, precision):
    with open('test.geojson') as f:
        data = json.load(f)

    features = data['features']
    points = [
        geo['geometry']["coordinates"]
        for geo in features if pred(geo)
    ]
    print points
    ar_points = array(points).reshape(len(points) * 2, 2)
    print ar_points
    bandwidth = estimate_bandwidth(ar_points) / precision
    cluster = MeanShift(bandwidth=bandwidth)
    cluster.fit(ar_points)
    labels = cluster.labels_
    cluster_centers = cluster.cluster_centers_
    print 'clusters:', len(unique(labels))

    for i, geo in enumerate(filter(pred, features)):
        geo['geometry']["coordinates"] = [
            list(cluster_centers[labels[i*2 + j]])
            for j in range(2)
        ]

    with open(filename, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    from sys import argv
    filename = "test2.geojson"
    prec = 2
    make(filename, prec)

