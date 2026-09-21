import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from components.process import process


st.title("Sentiment Analysis App")

text=st.text_input("Enter the Sentence :")

if st.button("sentimentize"):
    st.spinner("Identifying the sentiment...")
    result=process(text)
    st.write(result)