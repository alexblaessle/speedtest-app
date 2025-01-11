import streamlit as st
import pandas as pd

st.title("Speedtest-app")

def load_data(fn):
    df=pd.read_csv(fn)
    df=df.melt(id_vars=['timestamp'])
    return df

df = load_data("speed_test_results.csv")

st.subheader("Download/upload speeds")
st.line_chart(data=df[~df['variable'].str.contains('ping')],x="timestamp",y="value",color='variable')

st.subheader("Ping")
st.line_chart(data=df[df['variable'].str.contains('ping')],x="timestamp",y="value",color='variable')

