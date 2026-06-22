import streamlit as st

st.set_page_config(
    page_title="Job Monitoring",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Job Monitoring Dashboard")

st.success("Deploy สำเร็จแล้ว 🎉")

col1, col2, col3 = st.columns(3)

col1.metric("Running", 0)
col2.metric("Success", 0)
col3.metric("Failed", 0)
