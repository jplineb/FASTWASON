# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:50:21 2019

@author: jplineb
"""

import os
import pandas as pd
import shutil
import numpy as np
import random

wrkingdir = os.getcwd()
df = pd.read_csv("listof_TrainandTestData.csv")



# Seperate the frames such that some videos are reserved for validation
newcolumns = ["Quality", "External_ID", "File_Name", "Frame_Number", "destination"]
qualities = [(1,"\Quality1", "labeledquality1"), (2, "\Quality2", "labeledquality2"), (3, "\Quality3", "labeledquality3"), (4, "\Quality4", "labeledquality4"),
             (5, "\Quality5", "labeledquality5")]




Qs = [1,2,3,4,5]
df = df.reindex(columns=newcolumns)


def getvideonames(row):
    videonameslist = []
    videonameslist.append(row) 
    videonameslist = list(videonameslist)
    return videonameslist

#def bracketdelete(filename):   
#    filename = filename.replace('[',' ').replace('[',' ')
#    filename = filename.split(' ')[1]
#    return filename 


def flattenlist(listofstuff):
    flat_list = []
    for sublist in listofstuff:
        for item in sublist:
            flat_list.append(item)
    return(flat_list)
        
def copyfiles(root, file, endpoint):
    frameloc = os.path.join(root, file)
    shutil.copy(frameloc, endpoint)

for q,f,l in qualities:
    classdirect = wrkingdir + "\\" + l
    dfSS = df.loc[df["Quality"] == q]
    dfSS = dfSS.drop_duplicates(["File_Name"])
    videonameslist = dfSS.File_Name.apply(getvideonames)
    alpha = list(videonameslist)
    flat_list = flattenlist(alpha)
    random.shuffle(flat_list)
    split1 = int(0.8 * len(flat_list)) # 80% split for the training data
    split2 = int(len(flat_list) - split1) # 20% split for the validation
    print('Amount of files')
    print(len(flat_list))
    print('Split Total ') 
    print(split1+split2) # these 4 lines check to see if the split total is equal to the original length of the list
    train_filenames = flat_list[:split1]
    test_filenames = flat_list[split1:]
    trainfolder = wrkingdir + f + ('_Train')
    testfolder = wrkingdir + f + ('_Test')
    if not os.path.exists(trainfolder): # creates the path for Training set folder
       os.makedirs(trainfolder)
    if not os.path.exists(testfolder):
       os.makedirs(testfolder)
    for root, dirs, files in os.walk(classdirect):
        for file in files:
            if file.startswith(tuple(train_filenames)):
                frameloc = os.path.join(root, file)
                shutil.copy(frameloc, trainfolder)
            else:
               frameloc = os.path.join(root, file)
               shutil.copy(frameloc, testfolder)
   
     
   
   















#traininglist = [trainimagesQ1, trainimagesQ2, trainimagesQ3, trainimagesQ4, trainimagesQ5]
#testlist = [testimagesQ1, testimagesQ2, testimagesQ3, testimagesQ4, testimagesQ5]
#trainingfolders = ["./Quality1_Test", "./Quality2_Test", "./Quality3_Test", "./Quality4_Test",
#                   "./Quality5_Test"]
#
#
#
#
#
#
#
#
#
#
#
## Copies over files
#
#
#def copyfiles(root, file, endpoint):
#    frameloc = os.path.join(root, file)
#    shutil.copy(frameloc, endpoint)
#
#
#
#for root, dirs, files in os.walk(wrkingdir):
#    for file in files:
#        for x in trainingfolders:
#            for y in traininglist:
#                if file.endswith(tuple(y)):
#                    copyfiles(root, file, y)
#            










