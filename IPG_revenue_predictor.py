# Author: Roland Pineda
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

mlr_intercept = 341215

option = st.selectbox(
    'Select Annual Income Range:',
    ('0-500K', '500K-1.5M', '1.5M-5M', '5M and above'))
st.write('You selected:', option)
if option == '0-500K':
    mlr_income = -149556
elif option == '500K-1.5M':
    mlr_income = -102413
elif option == '1.5M-5M':
    mlr_income = 7988
elif option == '5M and above':
    mlr_income = 243982

option = st.selectbox(
    'Select Net Worth Range:',
    ('0-5M', '5M-25M', '25M-100M', '100M and above'))
st.write('You selected:', option)
if option == '0-5M':
    mlr_net = -97647
elif option == '5M-25M':
    mlr_net = -98968
elif option == '25M-100M':
    mlr_net = 2917
elif option == '100M and above':
    mlr_net = 193698

option = st.selectbox(
    'Select Age Band:',
    ('0-18', '19-30', '31-50', '51-65', '65 and above'))
st.write('You selected:', option)

if option == '0-18':
    mlr_age = -19213
elif option == '19-30':
    mlr_age = -58525
elif option == '31-50':
    mlr_age = -9790
elif option == '51-65':
    mlr_age = 19901
elif option == '65 and above':
    mlr_age = 67627

option = st.selectbox(
    'Select Number of Children:',
    ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '>9'))
st.write('You selected:', option)

if option == '0':
    mlr_children = 0
elif option == '1':
    mlr_children = 11373
elif option == '2':
    mlr_children = 22746
elif option == '3':
    mlr_children = 34119
elif option == '4':
    mlr_children = 45492
elif option == '5':
    mlr_children = 56865
elif option == '6':
    mlr_children = 68238
elif option == '7':
    mlr_children = 79611
elif option == '8':
    mlr_children = 90984
elif option == '9':
    mlr_children = 102357
elif option == '>9':
    mlr_children = 0

option = st.selectbox(
    'Select Residency Region:',
    ('Asia', 'Europe', 'Middle East & Africa', 'North America', 'Pacific'))
st.write('You selected:', option)

if option == 'Asia':
    mlr_region = 10304
elif option == 'Europe':
    mlr_region = 38459
elif option == 'Middle East & Africa':
    mlr_region = 57865
if option == 'North America':
    mlr_region = -130861
elif option == 'Pacific':
    mlr_region = 24232

result =""
# assessment button
if st.button("Predict"):
	revenue = mlr_intercept + mlr_income + mlr_net + mlr_age + mlr_children + mlr_region
	st.success('**Predicted Revenue: $ {}'.format(revenue))