import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(page_title="Placement Dashboard", layout="wide")

# Title
st.title("🎓 Smart Placement Insights System")

# Load data
df = pd.read_csv("placement_data.csv")

# Sidebar filter
st.sidebar.title("🔍 Filter")
option = st.sidebar.selectbox("Select Data", ["All", "Placed Only"])

if option == "Placed Only":
    df = df[df['placed'] == 'Yes']

# Show dataset
st.subheader("📊 Dataset Preview")
st.write(df)

# Convert placed column
df['placed_num'] = df['placed'].map({'Yes':1, 'No':0})

# Placement rate
placement_rate = df['placed_num'].mean() * 100
st.subheader("📈 Placement Rate")
st.write(f"{placement_rate:.2f}%")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 CGPA vs Salary")
    st.scatter_chart(df[['cgpa', 'salary']])

with col2:
    st.subheader("📊 Placement Count")
    st.bar_chart(df['placed'].value_counts())

# Internship impact
st.subheader("🎯 Internships Impact")
st.bar_chart(df.groupby('internships')['placed_num'].mean())

# Insights
st.subheader("📌 Key Insights")
st.write("""
- Higher CGPA increases placement chances  
- Internships improve placement probability  
- Skilled students (Python, SQL) get better opportunities  
- Higher CGPA → Higher salary trend  
""")
