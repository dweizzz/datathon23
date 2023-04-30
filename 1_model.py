import requests
import json
import streamlit as st
import pandas as pd
import numpy as np

st.title('Our final Model')
st.divider()

country_options = ['Australia', 'Austria', 'Belgium', 'Canada', 'Czech Republic', 
'Finland', 'France', 'Germany', 'Hungary', 'Iceland', 'Ireland', 'Italy', 'Japan', 'Korea', 'Luxembourg', 
'Mexico', 'Netherlands', 'New Zealand', 'Poland', 'Spain', 'Switzerland', 'United Kingdom', 'United States', 
'Estonia', 'Israel', 'Slovenia', 'Latvia', 'Lithuania']

country = st.selectbox('Select a country', country_options)
options = ['Density Physicians','Number Hospitals','Medium Wage', "'Number of Pharmacists"]

target_resource = st.radio('What should the target resource be?', options)

year = st.slider('Choose a year', 2021,2030, 2025)

number = st.slider('Immunization Goal', 80.0,100.0, 85.0)

