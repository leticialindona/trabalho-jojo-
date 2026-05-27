import streamlit as st
import pandas as pd 

st.title("Filmes da barbie")

df = pd.read_csv("barbie_filmes.csv")
st.write(df)
st.subheader("Nota dos filmes")
st.bar_chart(df.set_index("filme")["nota"])
                        
