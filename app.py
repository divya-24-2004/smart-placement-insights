import streamlit as st
import pandas as pd

df = pd.read_csv("placement_data.csv")

st.title("🎓 Smart Placement Insights System")

st.subheader("Dataset Preview")
st.write(df)

st.subheader("Placement Rate")
placement_rate = df['placed'].map({'Yes':1,'No':0}).mean()*100
st.write(f"{placement_rate:.2f}%")

st.subheader("CGPA vs Salary")
st.scatter_chart(df[['cgpa','salary']])

st.subheader("Students by Placement")
st.bar_chart(df['placed'].value_counts())