import streamlit as st
import pandas as pd
from datetime import datetime

FILE = "portfolio.csv"

if FILE not in st.session_state:
    try:
        st.session_state.df = pd.read_csv(FILE)
    except:
        st.session_state.df = pd.DataFrame(
            columns=["Date","Symbol","Type","Price","Qty"]
        )

df = st.session_state.df

st.title("📊 Portfolio Dashboard")

# ---- BUY ----
st.subheader("➕ Buy / Sell")

with st.form("trade"):
    date = st.date_input("Date")
    symbol = st.text_input("Symbol").upper()
    ttype = st.selectbox("Type",["BUY","SELL"])
    price = st.number_input("Price",0.0)
    qty = st.number_input("Quantity",1)
    submit = st.form_submit_button("Save")

    if submit:
        df.loc[len(df)] = [
            date.strftime("%Y-%m-%d"),symbol,ttype,price,qty
        ]
        df.to_csv(FILE,index=False)
        st.success("Saved")

# ---- STATUS ----
st.subheader("📈 Holdings")
st.dataframe(df)
