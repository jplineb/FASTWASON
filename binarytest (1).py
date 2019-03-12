
# Cell Dedicated to imports #
import os
import json
from watson_developer_cloud import VisualRecognitionV3
from prettytable import PrettyTable
import pandas as pd

# Defining Locations #

Class_Tested = 'Crap' # ONLY FILL OUT IF A CLASS IS BEING TESTED otherwise 'null'

Crap_folder = './crap/test/'
Notcrap_folder = './notcrap/test/'
Test_imgs_crap = os.listdir(Crap_folder) # list test img names
Test_imgs_notcrap = os.listdir(Notcrap_folder) # list test img names
FASTWATSON8_test_img_loc_crap = [('crap', Crap_folder + x) for x in Test_imgs_crap] # stores the location of each image 
FASTWATSON8_test_img_loc_notcrap = [('not_crap', Notcrap_folder + x) for x in Test_imgs_notcrap] # stores the location of each image 
FASTWATSON8_test_img_loc = FASTWATSON8_test_img_loc_crap + FASTWATSON8_test_img_loc_notcrap
amount_imgs = len(FASTWATSON8_test_img_loc) # check step

# Visual Recognition Test #
visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey='apikey')

outputs = []
results = pd.DataFrame([], columns = ['actual_class', 'predicted_class', 'score', 'img_name'])
Images_ran = 0

ctr = 0
for z in FASTWATSON8_test_img_loc:  
    print("Processing image", ctr+1, "of" ,amount_imgs)
    with open(z[1], 'rb') as image_file:
        classes = visual_recognition.classify(image_file, threshold= '0', owners=["me"]).get_result()
    outputs = (classes['images'][0])
    predicted_img_class_watson = outputs['classifiers'][0]['classes'][0]['class']
    score = outputs['classifiers'][0]['classes'][0]['score']
    img_name = outputs['image']
    results = results.append({'actual_class': z[0],  
                            'predicted_class': predicted_img_class_watson, 
                            'score': score, 
                            'img_name': img_name}, ignore_index = True)
    ctr = ctr + 1
results.to_csv('./test_results.csv')
    

#
## Pretty Table Output #
#
#Ptty_Tble = PrettyTable()
#
#if Class_Tested != 'null':
#  Ptty_Tble.field_names = ["True Image Class" , "Predicted Image Class", "Score", "Image Name"]
#else:
#  Ptty_Tble.field_names = ["Predicted Image Class", "Score", "Image Name"]
#  
#print(Ptty_Tble)
