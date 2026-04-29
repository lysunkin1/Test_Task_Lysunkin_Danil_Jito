import streamlit as st

st.title("Minimal Accounting App")

menu = st.sidebar.selectbox("Menu", ["Create Transaction", "View Transactions", "Reports"])

if menu == "Create Transaction":
    st.header("Create Transaction")

elif menu == "View Transactions":
    st.header("Transactions")

elif menu == "Reports":
    st.header("Reports")