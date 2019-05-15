# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:44:00 2019

@author: jplineb
"""


import pandas as pd
import numpy as np
import json
import os

# loads in data frames
filesindir = os.listdir()
watsoncsvlocation = filesindir[3]
labelboxcsvlocation = filesindir[1]
dfwatson = pd.read_csv(watsoncsvlocation)
dflabelbox = pd.read_csv(labelboxcsvlocation)


# shrinks labelbox data frame
df2labelbox = dflabelbox.drop(["ID", "DataRow ID", "Labeled Data", "Created By",
                              "Project Name", "Created At", "Seconds to Label", "Agreement",
                              "Dataset Name", "Reviews", "View Label"], axis=1)
df3labelbox = df2labelbox.drop(list(range(61)), axis = 0)

df4labelbox = df3labelbox.set_index('External ID', drop = False)

df5labelbox = df4labelbox.rename(columns = {'External ID' : 'img_name'})

# Joins the two data frames based on external ID as index

df = dfwatson.merge(df5labelbox, on = 'img_name')

# fixes label coloumn





def labelfix(jsons):
    labeldict = json.loads(jsons)
    quadrant = labeldict["quadrant"]
    
    return quadrant

df["Quadrant"] = df.Label.apply(labelfix)

df = df.drop("Label", axis=1)

df.to_csv("quadrant_confidence.csv")