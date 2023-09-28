#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 19:54:44 2023

@author: marcela
"""

import csv
import requests
import pandas as pd    

results = []
with open('/Users/marcela/Downloads/EBSCO_Package_links.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        results.append(row[1])

new_results = []
for url in results:   
    try:
        response= requests.head(url)   
        status= str(response.status_code)   
  
        new_results.append(url + "," + status)
    except Exception:
        pass
pd.Series(list(new_results)).to_csv("/Users/marcela/Downloads/EBSCO_Package_links.csv", index=False)
