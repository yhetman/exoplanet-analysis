#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans , whiten
from math import sqrt, ceil

def read_database():
    df = pd.read_csv('./planets_db.csv')
    planets_df = df[['pl_name', 'pl_orbper','pl_orbsmax','pl_bmassj',
        'pl_radj','pl_dens','ra','dec','st_optmag','st_dist',
        'st_teff','st_mass','st_rad']]
    db = planets_df.dropna()
    db = db.reset_index()
    db = pd.DataFrame.drop(db,'index', axis=1)
    db.columns = ['Planet','Period','Orbit Semi-Major Axis',
            'Mass','Radius','Density','Ascension','Declination',
            'Solar Brightness','Distance','Temperature',
            'Solar Mass','Solar Radii']
    return db


def creat_matrix(db):
    db = db.rename(index = db['Planet'])
    db = pd.DataFrame.drop(db,'Planet', axis=1)
    dataMatrix = db.values
    return dataMatrix


def define_centrioids(dataMatrix):
    stdev = np.std(dataMatrix, axis = 0)
    whitened = whiten(dataMatrix)
    #st = "======"
    #for i in range(len(dataMatrix)):
    #    print (dataMatrix[i],st,whitened[i])
    means, _ = kmeans(whitened, 36)
    unwhitened = stdev * means
    unwhitened = list(map(tuple, unwhitened))
    unwhitened.sort()
    return unwhitened


def count_distance(a, b):
    (a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12) = a
    (b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12) = b
    dist = sqrt((a1 - b1)**2 + (a2 - b2)**2 + (a3 - b3)**2 + (a4 - b4)**2 + (a5 - b5)**2 + (a6 - b6)**2 + (a7 - b7)**2 +(a8 - b8)**2 +(a9 - b9)**2 + (a10 - b10)**2 + (a11 - b11)**2 +(a12 - b12)**2)
    return dist


def count_matches(centers, dataMatrix):
    matches = [0] * (len(centers))
    for i, a in enumerate(dataMatrix):
        #print (i, "===", row)
        #for a in row:
           # print(a)
        distances = [count_distance(a, b) for b in centers]
        min_index = distances.index(min(distances))
        matches[min_index] += 1
    return matches


def main():
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_rows', None)
    #np.set_printoptions(threshold = np.inf)
    db = read_database()
    dataMatrix = creat_matrix(db)
    centrioids = define_centrioids(dataMatrix)
    matches = count_matches(centrioids, dataMatrix)
    #max_count = max(matches)

    db = db.rename(index = db['Planet'])
    db = pd.DataFrame.drop(db,'Planet', axis=1)
    columns = db.columns
    n_rows = len(centrioids)
    fig, axs =plt.subplots(2,1)
    axs[0].axis('tight')
    axs[0].axis('off')
    the_table = axs[0].table(cellText = centrioids, colLabels = columns, loc='center')
#   axs[1].plot(clust_data[:,0],clust_data[:,1])
    nb_rows = range(len(centrioids))
    axs[1].bar(nb_rows, matches, tick_label = nb_rows, width = 0.8, color = ['blue', 'green']) 
    plt.xlabel('Clusters') 
    plt.ylabel('Number of planets') 
    plt.title('Clustering of exoplanets')
    plt.show()
    print(centrioids)

#   rows = ['%d cluster' % (x + 1) for x in range(n_rows)]
#   index = np.arange(len(columns)) + 0.3
#   bar_width = 0.4
#   y_offset = np.zeros(len(columns))
#   cell_text = []
#   for row in range(n_rows):
#       plt.bar(index, centrioids[row], bar_width, bottom = y_offset)
#       y_offset += centrioids[row]
#       cell_text.append(['%1.1f' % x for x in y_offset])
#       cell_text.reverse()
#   the_table = plt.table(cellText = cell_text, rowLabels = rows, colLabels=columns, loc='bottom')
#   plt.subplots_adjust(left=0.2, bottom=0.2)
#   prop1 = 'Density'
#   prop2 = 'Declination'
#   X = db[[prop1,prop2]]
#   sns.set()
#   plt.scatter(X[prop1], X[prop2], c='black')
#   plt.xlabel(prop1)
#   plt.ylabel(prop2)
#   plt.show()

if __name__ == "__main__":
    main()
