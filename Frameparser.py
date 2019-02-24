# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:03:22 2018

@author: jline
"""

import os
import shutil
wrkingdirect = os.getcwd()
allwantedframes = []
#filetype = '.png'
framelist = ('e22.png','e44.png','e66.png','e88.png', 'e110.png', 'e132.png', 'e154.png', 'e176.png')
#framelist_ft = (x + filetype for x in framelist)
for root, dirs, files in os.walk(wrkingdirect):
    for file in files:   
        if file.endswith(framelist):
            frameloc = os.path.join(root,file) # Location of the saved frame
            allwantedframes.append(frameloc) # adds grabbed frames to a list
            newsaveloc = (wrkingdirect + '\FASTFRAMES8')
            if not os.path.exists(newsaveloc): # checks if directory exists
                os.makedirs(newsaveloc)
            shutil.copy(frameloc, newsaveloc) # copies file from whole data set into sampled data set
