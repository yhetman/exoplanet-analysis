#!/usr/bin/env python3
import csv
import pandas as pd

with open('planets_db.csv', encoding='utf-8-sig') as csvfile:
    data = list(csv.DictReader(csvfile))

#for di in data:
#    print(di)
print("There are %d dictionaries" % len(data))
print(data[0].keys())
