import pandas as pd
import streamlit as st

st.title('Dashboard')

uploaded_file = st.sidebar.file_uploader("Choose a Revolut CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['df'] = df
    
