# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:00:56 2019

@author: John Paul
"""

import csv
import os
import shutil

wrkingdirect = os.getcwd()
sourcefolder = '/FASTFRAMES8/'

fetchloc = wrkingdirect + sourcefolder
newsavenotcrap = wrkingdirect + '/notcrap/'
newsavecrap = wrkingdirect + '/crap/'

if not os.path.exists(newsavecrap):
    os.makedirs(newsavecrap)
if not os.path.exists(newsavenotcrap):
    os.makedirs(newsavenotcrap)

with open('export.csv', 'r') as f:
    reader = csv.reader(f)
    thelist = list(reader)
    
print(thelist)
notcraplist = []
craplist = []
frameswantednotcrap =  []
frameswantedcrap = []

for x in thelist:
    for a in x:
        if a == ('{"quality":"not_crap"}'):
            notcraplist.append(x)
        if a == ('{"quality":"crap"}'):
            craplist.append(x)
            
            
for x in notcraplist:
    a = x[8]
    frameswantednotcrap.append(a)
    
for x in craplist:
    a =x[8]
    frameswantedcrap.append(a)

for root, dirs, files in os.walk(fetchloc):
    for file in files:
        if file.endswith(tuple(frameswantednotcrap)):
            frameloc = os.path.join(root, file)
            shutil.copy(frameloc, newsavenotcrap)
        if file.endswith(tuple(frameswantedcrap)):
            frameloc = os.path.join(root, file)
            shutil.copy(frameloc, newsavecrap)
            
framecompare = list(set(frameswantedcrap) & set(frameswantednotcrap)) # compares the lists for anyh overlap
for root, dirs, files in os.walk(newsavecrap): #  deletes the overlapped frame in the crap folder
    for file in files:
        if file.endswith(tuple(framecompare)):
            frameloc = os.path.join(root, file)
            os.remove(frameloc)
            