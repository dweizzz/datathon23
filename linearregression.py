# -*- coding: utf-8 -*-
"""LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/dweizzz/datathon23/blob/main/LinearRegression.ipynb
"""

import numpy as np
import matplotlib as plot
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from functools import reduce
import matplotlib.pyplot as plt

"""#Dataframes"""

def dataCleaning():
    #Immunization dataframe
    df_immunizations = pd.read_csv('/Users/andreasiby/CDS/datathon23/data/Immunisations.csv')
    df_immunizations=df_immunizations[['Country','Year','Value']]
    df_immunizations=df_immunizations.rename(columns={'Value': 'Immunization'})
    df_immunizations

    #density physicians
    df_physicians = pd.read_csv('/Users/andreasiby/CDS/datathon23/data/Physicians.csv')
    df_physicians = df_physicians[df_physicians['Variable'] == 'Practising physicians']
    df_physicians = df_physicians[df_physicians['Measure'] == 'Density per 1 000 population (head counts)']
    df_physicians=df_physicians[['Country','Year','Value']]
    df_physicians = df_physicians.rename(columns={'Value': 'Density Physicians'})
    df_physicians

    #hospitals dataframe
    df_hospitals = pd.read_csv('/Users/andreasiby/CDS/datathon23/data/Hospitals.csv')
    df_hospitals.reset_index(inplace=True)  # Reset the index to a simple integer index
    df_hospitals=df_hospitals[['index','Country','Year','Variable','Value']]
    df_hospitals = df_hospitals.groupby(['Country', 'Year'])['Value'].sum().reset_index()
    df_hospitals = df_hospitals.rename(columns={'Value': 'Number Hospitals'})
    df_hospitals

    #medium wage dataframe
    df_medwage = pd.read_csv('/Users/andreasiby/CDS/datathon23/data/MedianWage.csv')
    df_medwage=df_medwage[df_medwage['Series'] == '2021 constant prices and NCU']
    df_medwage=df_medwage[['Country','Time','Unit Code','Value']]
    df_medwage = df_medwage.rename(columns={'Value': 'Median Wage','Time':'Year'})
    df_medwage

    df_pharm = pd.read_csv('/Users/andreasiby/CDS/datathon23/data/pharmacists.csv')
    df_pharm = df_pharm[df_pharm['Variable'] == 'Practising pharmacists']
    df_pharm = df_pharm[df_pharm['Measure'] == 'Number of persons (head counts)']
    df_pharm = df_pharm[['Country','Year','COU','Value']]
    df_pharm = df_pharm.rename(columns={'Value': 'Number Pharmacists','Time':'Year'})
    df_pharm
    
    """#Combining Variable Dataframes"""

    dfs = [df_immunizations,df_physicians, df_hospitals, df_medwage,df_pharm]

    #merge all DataFrames into one
    all_vars = reduce(lambda left, right: pd.merge(left, right, on=['Country', 'Year'], how='inner'), dfs)
    all_vars.sort_values('Country')
    return all_vars





def model(country, all_vars):
    """#Linear Regression Model"""

    country_specific = all_vars[all_vars['Country'] == 'Australia']

    y = country_specific['Immunization']
    X = country_specific[['Year', 'Density Physicians','Number Hospitals','Median Wage','Number Pharmacists']]
    X['Density Physicians Sqrt'] = np.sqrt(X['Density Physicians'])
    #X['Num_Physicians_Sq'] = country_specific['Num_Physicians'] ** 2
    X['Number Hospitals Sqrt'] = np.sqrt(X['Number Hospitals'])

    # Add a constant term to the independent variables to represent the intercept
    X = sm.add_constant(X)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create the OLS model
    model = sm.OLS(y_train, X_train)

    # Train the model using the fit method
    results = model.fit()

    # Predict values for the test set
    y_pred = results.predict(X_test)

    summary = results.summary()
    return [y_test, y_pred]

