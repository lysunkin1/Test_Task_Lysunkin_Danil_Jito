import streamlit as st

st.title("Minimal Accounting App")

menu = st.sidebar.selectbox("Menu", ["Create Transaction", "View Transactions", "Reports"])

if menu == "Create Transaction":
    st.header("Create Transaction")

elif menu == "View Transactions":
    st.header("Transactions")

elif menu == "Reports":
    st.header("Reports")

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if menu == "Create Transaction":
    st.header("Create Transaction")

    t_type = st.selectbox("Type", ["Revenue", "Expense"])
    amount = st.number_input("Amount", min_value=0.0)
    partner = st.text_input("Partner")

    if st.button("Submit"):
        transaction = {
            "type": t_type,
            "amount": amount,
            "partner": partner,
        }

        st.session_state.transactions.append(transaction)
        st.success("Transaction created!")

elif menu == "View Transactions":
    st.header("Transactions")

    for t in st.session_state.transactions:
        st.write(t)

ACCOUNTS = {
    "cash": 1000,
    "receivable": 1100,
    "payable": 2000,
    "revenue": 4000,
    "expense": 5000,
}

if "entries" not in st.session_state:
    st.session_state.entries = []