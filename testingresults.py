# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 16:23:56 2019

@author: John Paul
"""

import pandas as pd
from sklearn.metrics import roc_auc_score

df = pd.read_csv('./test_results.csv')

df = df.drop('Unnamed: 0', axis=1)

df['actual_class_code']=1
df.actual_class_code[df.actual_class=='not_crap'] = 0

print(roc_auc_score(df.actual_class_code, df.score))