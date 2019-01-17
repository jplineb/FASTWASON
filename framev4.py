# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:04:07 2018

@author: John Paul
"""

import os
import cv2
import zipfile
filecount = 0
fileelem = []
wrkingdirect = os.getcwd()
count = 0
counter = 1
for root, dirs, files in os.walk(wrkingdirect): # unzipping of zipped folders #
    for file in files:
        if file.endswith('.zip'):  # Unzips if zip files are present #
            zip = zipfile.ZipFile(os.path.join(root,file))
            zip.extractall(root)
wrkingdirect = os.getcwd() #refreshes the directory#
for root, dirs, files in os.walk(wrkingdirect):
    for file in files:
        if file.endswith('.mp4'): # finds files with .mp4 file extension #
            vidlocat = os.path.join(root,file) # Guves the specific location of the video in question #
            cap = cv2.VideoCapture(vidlocat) # captures the video at said location #
            count = 0
            counter += 1
            success = True
            fileelem.append(vidlocat) # adds the videos to a list of directories pointing at the videos that have had frames extracted #
            gendirec = root+'/'+ file + '_' + 'Generated' # creates the file strucure #
            os.mkdir(gendirec) # Creates the directory to store the video frames #
            while success: # while loop that keeps generating frames until the end of the video #
                success, image = cap.read()
                print('read a new frame:', success) # prints the outcome of 1 frame generation #
                cv2.imwrite(gendirec +'/' + file  +'__' + 'frame%d.png' %count, image) # saves the frames of the video #
                count += 1
                
    
            
            
            
# =============================================================================
# pathOut = wrkingdirect + r'/output/'
# count = 0
# counter = 1
# listing = os.listdir(r'videos')
# for vid in listing:
#    video = wrkingdirect + r'/videos/' + vid
#    cap = cv2.VideoCapture(video)
#    count = 0
#    counter += 1
#    success = True
#    while success:
#        success,image = cap.read()
#        print('read a new frame:',success)
#        cv2.imwrite(pathOut + str(vid) + '__' + 'frame%d.png' %count ,image)
#        count+=1
# =============================================================================
