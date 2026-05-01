# Minimal Accounting Web App

## Overview

This is a simple accounting web application built with Python and Streamlit.

The app allows creating basic transactions, generates journal entries using double-entry accounting, and provides simple financial reports.

---

## Features

* Create transactions (Revenue, Expense)
* Automatic journal entries (double-entry logic)
* View list of transactions
* Profit & Loss report
* Partner ledger

---

## Accounting Logic

Each transaction generates two journal entries:

Revenue:

* Debit: Accounts Receivable (1100)
* Credit: Revenue (4000)

Expense:

* Debit: Expense (5000)
* Credit: Cash (1000)

All reports are calculated based on journal entries.

---

## Tech Stack

* Python
* Streamlit
* Docker

---

## Run locally

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py

Open in browser:
http://localhost:8501

---

## Run with Docker

Build image:

docker build -t accounting-app .

Run container:

docker run -p 8501:8501 accounting-app

Open in browser:
http://localhost:8501

---

## Project Structure

* app.py — main application
* Dockerfile — container setup
* requirements.txt — dependencies
* prompt_history.md — prompt usage

---

## Notes

This is a simplified implementation intended to demonstrate core accounting concepts.

It does not include advanced features such as taxes, multi-currency, or reconciliation.
