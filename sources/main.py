#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.vq import kmeans , whiten
from read_db import read_database, create_matrix
from algorithm import * 

def draw_histogram(centers, matches):
    sns.set()
    fig, ax = plt.subplots(1,1)
    nb_rows = range(len(centers))
    axs[1].bar(nb_rows, matches, tick_label = nb_rows, width = 0.8, color = ['blue', 'green']) 
    plt.xlabel('Clusters') 
    plt.ylabel('Number of planets') 
    plt.title('Clustering of exoplanets')
    plt.show()

def main():
#   pd.set_option('display.max_columns', None)
#   pd.set_option('display.max_rows', None)
#   np.set_printoptions(threshold = np.inf)
    db = read_database()
    dataMatrix = create_matrix(db)
    centrioids = define_centrioids(dataMatrix)
    matches = count_matches(centrioids, dataMatrix)
#   max_count = max(matches)
    draw_histogram(centrioids, matches)
    db = db.rename(index = db['Planet'])
    db = pd.DataFrame.drop(db,'Planet', axis=1)
    columns = db.columns
#    n_rows = len(centrioids)
#    axs[0].axis('tight')
#    axs[0].axis('off')
#   the_table = axs[0].table(cellText = centrioids, colLabels = columns, loc='center')
#   axs[1].plot(clust_data[:,0],clust_data[:,1])
#    nb_rows = range(len(centrioids))
#    axs[1].bar(nb_rows, matches, tick_label = nb_rows, width = 0.8, color = ['blue', 'green']) 
#    plt.xlabel('Clusters') 
#    plt.ylabel('Number of planets') 
#    plt.title('Clustering of exoplanets')
#    plt.show()
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
