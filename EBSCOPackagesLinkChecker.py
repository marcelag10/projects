#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:16:38 2023

@author: marcela

https://brianli.com/2021/06/how-to-find-broken-links-with-python/
https://docs.python.org/3/howto/urllib2.html

"""

import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


#open csv file
def get_broken_links(): #Validate HTTP status code

    def _validate_url():
        with open('') as file_obj:
            read_file = csv.reader(file_obj)
            url=[1]
            for row in read_file:
                response=requests.head(url)
            if response.status_code== 404 or 500 or 503 or 301 or 400: #if the status code is any of these, I want to append the link to the broken_links list
                response=False  
                broken_links.append(url)
            
#Make request to URL                
data = requests.get(url).text #Executes the request

#Parse HTML
parshtml= BeautifulSoup(data, features="html.parser") 

links = [link.get("href") for link in soup.find_all("response=False") if f"//{root_domain}" in link.get("href")]

#List broken links 
broken_links=[]

#loop
with ThreadPoolExecutor(max_workers=20) as executor:
		executor.map(read_file, links)
get_broken_links() 

"""
Get broken links with defined function and set root domain
Use url, disable redirects, auth, proxies, timeout (3 secs)
"""
