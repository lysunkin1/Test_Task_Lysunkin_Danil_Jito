import streamlit as st

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "entries" not in st.session_state:
    st.session_state.entries = []

ACCOUNTS = {
    "cash": 1000,
    "receivable": 1100,
    "payable": 2000,
    "revenue": 4000,
    "expense": 5000,
}

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
st.title("Minimal Accounting App")

menu = st.sidebar.selectbox(
    "Menu", ["Create Transaction", "View Transactions", "Reports"]
)