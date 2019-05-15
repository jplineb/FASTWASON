# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:12:27 2019

@author: jplineb
"""

import os
import shutil
import random



wrkingdirect = os.getcwd() # Grabs the working direcory
classes =  ['labeledquality1', 'labeledquality2', 'labeledquality3', 'labeledquality4', 'labeledquality5'] #class folders


for x in range(len(classes)):
    n = x + 1
    filename = []
    classdirect = wrkingdirect + '\\' + classes[x] # finds where the classes foldeer is located
    trainfolder = 'Quality' + str(n) + '_Train'
    testfolder = 'Quality' + str(n) + '_Test'
    train_filenames = []
    test_filenames = []
    for roots,dirs,files in os.walk(classdirect):
        filename = files
    random.shuffle(filename)
    split1 = int(0.8 * len(filename)) # 80% split for the training data
    split2 = int(len(filename) - split1) # 20% split for the validation
    print('Amount of files')
    print(len(filename))
    print('Split Total ') 
    print(split1+split2) # these 4 lines check to see if the split total is equal to the original length of the list
    train_filenames = filename[:split1]
    test_filenames = filename[split1:]
    if not os.path.exists(trainfolder): # creates the path for Training set folder
        os.makedirs(trainfolder)
    if not os.path.exists(testfolder):
        os.makedirs(testfolder)
    for alpha in range(0, len(train_filenames)): # Copies over the file
        frameloc = classdirect + '\\' + train_filenames[alpha]
        shutil.copy(frameloc, trainfolder)
    for beta in range(0, len(test_filenames)):
        frameloc = classdirect + '\\' + test_filenames[beta]
        shutil.copy(frameloc, testfolder)
        
        
        
        
    