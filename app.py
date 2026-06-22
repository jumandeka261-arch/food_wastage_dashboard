import streamlit as st
import pandas as pd
import pyodbc

st.title("Food Wastage Management Dashboard")

# SQL Connection
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=LAPTOP-DU4AGPUL;"
    "DATABASE=FoodWastageDB;"
    "Trusted_Connection=yes;"
)

# Read Tables
providers = pd.read_sql("SELECT * FROM [providers_import (1)]", conn)
receivers = pd.read_sql("SELECT * FROM receivers_data", conn)
food = pd.read_sql("SELECT * FROM food_listings_import", conn)
claims = pd.read_sql("SELECT * FROM claims_import", conn)

# KPI Section
st.subheader("Dashboard KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Providers", len(providers))
col2.metric("Receivers", len(receivers))
col3.metric("Food Listings", len(food))
col4.metric("Claims", len(claims))

st.subheader("Providers Data")
st.dataframe(providers.head())

st.subheader("Receivers Data")
st.dataframe(receivers.head())
st.subheader("Food Data")
st.dataframe(food.head())

st.subheader("Claims Data")
st.dataframe(claims.head())

st.write("Food Columns:")
st.write(food.columns)
st.write(food.columns)


st.subheader("Providers Data")
st.dataframe(providers.head())

st.subheader("Receivers Data")
st.dataframe(receivers.head())

st.subheader("Food Data")
st.dataframe(food.head())

st.write("Food Columns:")
st.write(food.columns)

st.sidebar.title("Food Wastage Dashboard")
st.sidebar.success("Connected to SQL Server")


st.subheader("Provider Type Distribution")

provider_chart = providers["Type"].value_counts()
st.bar_chart(provider_chart)

st.subheader("Provider Type Distribution")

provider_chart = providers["Type"].value_counts()
st.bar_chart(provider_chart)

providers = pd.read_sql("SELECT * FROM [providers_import (1)]", conn)
receivers = pd.read_sql("SELECT * FROM receivers_data", conn)
food = pd.read_sql("SELECT * FROM food_listings_import", conn)
claims = pd.read_sql("SELECT * FROM claims_import", conn)