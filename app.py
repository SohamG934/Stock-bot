import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data
from datetime import date
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import streamlit as st

start ='2010-01-01'
end ='2022-6-3'

st.title('Stock Trend Prediction')

user_input=st.text_input("Enter Stock Ticker", "AAPL")
df=data.DataReader(user_input, 'yahoo', start, end)

#describing data
st.subheader("Data from 2010-2019")
st.write(df.describe())
