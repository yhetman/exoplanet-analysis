#!/usr/bin/env python3

import numpy as np
from math import sqrt, ceil
from scipy.cluster.vq import kmeans , whiten


def perform_kmeans(dataMatrix):
    whitened = whiten(dataMatrix)
    means, _ = kmeans(whitened, 10)
    return means


def define_centrioids(dataMatrix):
    stdev = np.std(dataMatrix, axis = 0)
    means = perform_kmeans(dataMatrix)
    unwhitened = stdev * means
    unwhitened = list(map(tuple, unwhitened))
    unwhitened.sort()
    return unwhitened


def count_distance(a, b):
    (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10) = a
    (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10) = b
    dist = sqrt((a1 - b1)**2 + (a2 - b2)**2 + (a3 - b3)**2 +
            (a4 - b4)**2 + (a5 - b5)**2 + (a6 - b6)**2 +
            (a7 - b7)**2 +(a8 - b8)**2 +(a9 - b9)**2 +
            (a10 - b10)*2)
    return dist


def count_matches(centers, dataMatrix):
    matches = [0] * (len(centers))
    for i, a in enumerate(dataMatrix):
#       print (i, "===", row)
#       for a in row:
#       print(a)
        distances = [count_distance(a, b) for b in centers]
        min_index = distances.index(min(distances))
        matches[min_index] += 1
    return matches

