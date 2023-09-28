#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:57:07 2023

@author: marcela
"""
import csv
import urllib


with open("/Users/marcela/Downloads/EBSCO_Package_links.csv", "r") as f:
    for row in csv.reader(f):
        urls= [x.rstrip() for x in f.readlines()]

        
def test_urls():
    for rows in urls:
        try:
               urllib.request.urlopen(urls)
        except urllib.error.HTTPError as e:     
            print(e.reason)

test_urls()