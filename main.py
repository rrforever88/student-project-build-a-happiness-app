import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")
columns = df.columns.values

st.title("In Search for Happiness")

x_axis = st.selectbox("Select the data for the X-axis",
                      (columns))
y_axis = st.selectbox("Select the data for the Y-axis",
                      (columns))

st.subheader(f"{x_axis} and {y_axis}")

x_axis_data = df[x_axis]
y_axis_data = df[y_axis]

figure = px.scatter(x=x_axis_data, y=y_axis_data, labels={"x": f"{x_axis}", "y": f"{y_axis}"})
st.plotly_chart(figure)
