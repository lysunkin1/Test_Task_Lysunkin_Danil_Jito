import streamlit as st

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "entries" not in st.session_state:
    st.session_state.entries = []

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



if "entries" not in st.session_state:
    st.session_state.entries = []

def create_entry(account, amount, entry_type, partner=None):
    return {
        "account": account,
        "amount": amount,
        "type": entry_type,
        "partner": partner,
    }
def post_revenue(amount, partner):
    return [
        create_entry(ACCOUNTS["receivable"], amount, "debit", partner),
        create_entry(ACCOUNTS["revenue"], amount, "credit", partner),
    ]
def post_expense(amount, partner):
    return [
        create_entry(ACCOUNTS["expense"], amount, "debit", partner),
        create_entry(ACCOUNTS["cash"], amount, "credit", partner),
    ]