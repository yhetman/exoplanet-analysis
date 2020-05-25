#!/usr/bin/env python3

import pandas as pd
import numpy as np

df = pd.read_csv('./planets_db.csv')

planets_df = df[['pl_name', 'pl_orbper','pl_orbsmax','pl_bmassj','pl_radj','pl_dens','ra','dec','st_optmag','st_dist','st_teff','st_mass','st_rad']]

db = planets_df.dropna()
db = db.reset_index()
db = pd.DataFrame.drop(db,'index', axis=1)
print(len(db))
print(db.head())
db.columns = ['Planet','Period','Orbit Semi-Major Axis','Mass','Radius','Density','Ascension','Declination','Solar Brightness','Distance','Temperature','Solar Mass','Solar Radii']
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
print(db.head())
db = db.rename(index=db['Planet'])
db = pd.DataFrame.drop(db,'Planet', axis=1)
DataMatrix = db.values
np.set_printoptions(threshold = np.inf)
print(DataMatrix)
