#!/usr/bin/env python3

import csv
import pandas as pd


def read_database():
    df = pd.read_csv('../planets_db.csv')
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


def create_matrix(db):
    db = db.rename(index = db['Planet'])
    db = pd.DataFrame.drop(db,'Planet', axis=1)
    dataMatrix = db.values
    return dataMatrix


