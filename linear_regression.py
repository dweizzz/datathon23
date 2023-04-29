import numpy as np
import matplotlib as plot
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split

#preprocessing
df = pd.read_csv('data\Immunisations.csv')
to_drop = ['VAR','UNIT','Measure','COU','YEA', 'Flag Codes','Flags']
df.drop(to_drop, inplace=True, axis=1)

#creating a separate dataframe with just the doctors  
df_doc = pd.read_csv('data\Physicians.csv')
to_drop = ['VAR','UNIT','Measure','COU','YEA', 'Flag Codes','Flags']
df_doc.drop(to_drop, inplace=True, axis=1)
df_doc = df_doc[df_doc['Variable'].str.contains('Practising physicians')]
merged = pd.merge(left=df, right=df_doc, how='right', left_on=['Year','Country'], right_on=['Year','Country'])
merged = merged.rename(columns={'Value_x': 'percent_immun', 'Value_y': 'num_physicians'})

#split data
train, test = train_test_split(merged, test_size=0.2)

#number of features to pass into model
num_features = len(merged.columns())

class LinearRegression(torch.nn.Module):

   def __init__(self):
        super(LinearRegression, self).__init__() 
        self.linear = nn.Linear(num_features, 1)
      
   def forward(self, x): 
        predict_y = self.linear(x) 
        return predict_y
   
model = LinearRegression(num_features, )