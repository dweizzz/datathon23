import numpy as np
import matplotlib as plot
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

class LinearRegression(torch.nn.Module):
   
   def preprocessing(self):
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
        LinearRegression.split(merged)

   def split(self, df):
        merged = df
        train_size = int(0.8 * len(merged))
        test_size = len(merged) - train_size
        train_dataset, test_dataset = torch.utils.data.random_split(merged, [train_size, test_size])

   def __init__(self):
        super(LinearRegression, self).__init__() 
        self.linear = nn.Linear(1, 1)
      
   def forward(self, x): 
        predict_y = self.linear(x) 
        return predict_y