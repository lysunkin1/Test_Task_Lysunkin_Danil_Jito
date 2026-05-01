import streamlit as st
from datetime import datetime

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
        create_entry(ACCOUNTS["payable"], amount, "credit", partner),
    ]

st.title("Minimal Accounting App")

menu = st.sidebar.selectbox(
    "Menu", ["Create Transaction", "View Transactions", "Reports"]
)

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
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }

        st.session_state.transactions.append(transaction)

        if t_type == "Revenue":
            entries = post_revenue(amount, partner)
        else:
            entries = post_expense(amount, partner)

        st.session_state.entries.extend(entries)

        st.success("Transaction created!")

elif menu == "View Transactions":
    st.header("Transactions")

    for t in st.session_state.transactions:
        st.write(t)

elif menu == "Reports":
    st.header("Reports")

    # Profit & Loss
    revenue = sum(
        e["amount"]
        for e in st.session_state.entries
        if e["account"] == ACCOUNTS["revenue"] and e["type"] == "credit"
    )

    expenses = sum(
        e["amount"]
        for e in st.session_state.entries
        if e["account"] == ACCOUNTS["expense"] and e["type"] == "debit"
    )

    st.subheader("Profit & Loss")
    st.write(f"Revenue: {revenue}")
    st.write(f"Expenses: {expenses}")
    st.write(f"Profit: {revenue - expenses}")

    # Partner Ledger
    ledger = {}

    for e in st.session_state.entries:
        partner = e["partner"]
        if not partner:
            continue

        if e["account"] not in [
            ACCOUNTS["receivable"],
            ACCOUNTS["payable"],
        ]:
            continue

        if partner not in ledger:
            ledger[partner] = 0

        if e["type"] == "debit":
            ledger[partner] += e["amount"]
        else:
            ledger[partner] -= e["amount"]

    st.subheader("Partner Ledger")

    for partner, balance in ledger.items():
        st.write(f"{partner}: {balance}")