#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 22:29:00 2023

@author: marcela
"""

import csv
import urllib

def test_urls():
    with open("/Users/marcela/Downloads/EBSCO_Package_links.csv", "r") as f:
        for row in csv.reader(f):
            urls= [x.rstrip() for x in f.readlines()]
    for rows in f:
        try:
            response = urllib.request.urlopen(urls, timeout=5).read().decode('utf-8')
            print(response)
        except urllib.error.HTTPError as e:     
            print(e.reason)

test_urls()
