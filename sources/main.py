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
    nb_rows = np.arange(1, len(centers) + 1, 1)
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
    the_table = ax.table(cellText = df.values,
                         rowLabels = df.index,
                         colLabels = df.columns,
                         colWidths=widths,loc = 'center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)
    the_table.scale(1,2)
    plt.show()

def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    np.set_printoptions(threshold = np.inf)
    db = read_database()
    dataMatrix = create_matrix(db)
    centrioids = define_centrioids(dataMatrix)
    matches = count_matches(centrioids, dataMatrix)
    df = create_DFrame(db, centrioids)
    draw_histogram(centrioids, matches)
    create_table(df)
    print(centrioids)

if __name__ == "__main__":
    main()
