# Author: Team4: Roland Pineda, Noemie Castro, Fabian Lim
# April 2023

import streamlit as st
# other libs
import numpy as np
import pandas as pd

# -- Set page config
apptitle = 'Howden IPG Revenue Predictor'
st.set_page_config(page_title=apptitle, page_icon='random',	
	layout= 'wide', 
	initial_sidebar_state="expanded")
# random icons in the browser tab

# give a title to your app
st.title('Howden IPG Revenue Predictor')

# Let's add a sub-title
st.write("A revenue predictor app")

mlr_intercept = 346366

option = st.selectbox(
    'Select Annual Income Range:',
    ('0-500K', '500K-1.5M', '1.5M-5M', '5M and above'))
st.write('You selected:', option)
if option == '0-500K':
    mlr_income = -139160
elif option == '500K-1.5M':
    mlr_income = -94730
elif option == '1.5M-5M':
    mlr_income = 3530
elif option == '5M and above':
    mlr_income = 230361

option = st.selectbox(
    'Select Net Worth Range:',
    ('0-5M', '5M-25M', '25M-100M', '100M and above'))
st.write('You selected:', option)
if option == '0-5M':
    mlr_net = -101202
elif option == '5M-25M':
    mlr_net = -101491
elif option == '25M-100M':
    mlr_net = -6780
elif option == '100M and above':
    mlr_net = 209473

option = st.selectbox(
    'Select Age Band:',
    ('0-18', '19-30', '31-50', '51-65', '65 and above'))
st.write('You selected:', option)

if option == '0-18':
    mlr_age = -19591
elif option == '19-30':
    mlr_age = -58465
elif option == '31-50':
    mlr_age = -17438
elif option == '51-65':
    mlr_age = 21017
elif option == '65 and above':
    mlr_age = 74478

option = st.selectbox(
    'Select Number of Children:',
    ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '>9'))
st.write('You selected:', option)

if option == '0':
    mlr_children = 0
elif option == '1':
    mlr_children = 12479
elif option == '2':
    mlr_children = 24958
elif option == '3':
    mlr_children = 37437
elif option == '4':
    mlr_children = 49916
elif option == '5':
    mlr_children = 62395
elif option == '6':
    mlr_children = 74874
elif option == '7':
    mlr_children = 87353
elif option == '8':
    mlr_children = 99832
elif option == '9':
    mlr_children = 112311
elif option == '>9':
    mlr_children = 0

option = st.selectbox(
    'Select Residency Region:',
    ('Asia', 'Europe', 'Middle East & Africa', 'North America', 'Pacific'))
st.write('You selected:', option)

if option == 'Asia':
    mlr_region = 817
elif option == 'Europe':
    mlr_region = 42998
elif option == 'Middle East & Africa':
    mlr_region = 54480
if option == 'North America':
    mlr_region = -129295
elif option == 'Pacific':
    mlr_region = 31000

result =""
# assessment button
if st.button("Predict"):
	revenue = mlr_intercept + mlr_income + mlr_net + mlr_age + mlr_children + mlr_region
	st.success('**Predicted Revenue: $ {:,}'.format(revenue))
