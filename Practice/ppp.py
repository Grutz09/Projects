import streamlit as st
import pandas as pd

st.write("""
         # My First App
         # Hello *world*
         """
         )

wine = pd.read_csv(r"C:\Users\seanandrew\Desktop\kaggle_datasets\winemag-data-130k-v2.csv", index_col=0)
# winer = wine.loc([(wine.country('Italy')) & (wine.points>90)])

st.line_chart(wine.country)
