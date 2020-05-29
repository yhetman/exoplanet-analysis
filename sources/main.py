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
    ax.bar(nb_rows, matches, tick_label = nb_rows, width = 0.8, color = ['blue', 'green']) 
    plt.xlabel('Clusters') 
    plt.ylabel('Number of planets') 
    plt.title('Clustering of exoplanets')
    plt.show()


def create_DFrame(db,centrioids):
    db = db.rename(index = db['Planet'])
    db = pd.DataFrame.drop(db,'Planet', axis=1)
    n_rows = len(centrioids)
    cell_text = []
    y_offset = np.zeros(len(db.columns))
    for row in range(n_rows):
        y_offset += centrioids[row]
        cell_text.append(['%.3f' % x for x in y_offset])
        cell_text.reverse()
    rows = pd.Index(['%d cluster' % (x + 1) for x in range(n_rows)])
    DFrame = pd.DataFrame(cell_text, columns = db.columns,index = rows)
    print(DFrame)
    return DFrame

def create_table(df):
    sns.set()
    fig, ax = plt.subplots()
#    n_rows = len(centrioids)
    ax.margins(0.1,0.1)
    ax.axis('tight')
    ax.axis('off')
    widths = []
    for i in df.columns:
        print(len(i), i)
        k = len(i)
        if k < 10:
            k = 10
        widths.append(k/120)
#    bar_width = 0.4
    the_table = ax.table(cellText = df.values, rowLabels = df.index, colLabels = df.columns, colWidths=widths,loc = 'center')
#    the_table = ax.table(df.values, colWidths=widths,rowLabels=df.index, colLabels=df.columns, loc='center')
#    the_table = ax.table(cellText = centrioids, colLabels = columns, loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1,3)
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
    df = create_DFrame(db, centrioids)
#    draw_histogram(centrioids, matches)
    create_table(df)
#    n_rows = len(centrioids)
#    axs[0].axis('tight')
#    axs[0].axis('off')
#   the_table = axs[0].table(cellText = centrioids, colLabels = columns, loc='center')
#   axs[1].plot(clust_data[:,0],clust_data[:,1])
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
