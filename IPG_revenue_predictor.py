# Author: Roland Pineda
# April 2023

import streamlit as st
# other libs
import numpy as np
import pandas as pd


income = st.radio(
    'Select Annual Income Range:'
    ("0-500K", "500K-1.5M", "1.5M to 5M", "5M and above"))
st.write("Client's annual income is within {income}!")

net_worth = st.radio(
    'Select Annual Income Range:'
    ("0-500K", "500K-1.5M", "1.5M to 5M", "5M and above"))
st.write("Client's annual income is within {net_worth}!")

