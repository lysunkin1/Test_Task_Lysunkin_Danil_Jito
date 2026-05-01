# Prompt History

This document captures the key prompts used during the development of the minimal accounting web application.
The prompts are grouped by development stages and reflect an iterative problem-solving approach.

---

## Step 1 — Understanding the domain

**Prompt 1:**
Explain the basics of double-entry accounting in simple terms (debit, credit, accounts, transactions).

**Prompt 2:**
Provide a few concrete examples of how business events (sales, expenses) are translated into accounting entries.

**Prompt 3:**
What is the difference between revenue, expense, receivables, and payables in a simplified system?

**Outcome:**
Established a working understanding of double-entry accounting and how business events translate into balanced journal entries.

---

## Step 2 — Defining the product scope

**Prompt 1:**
Propose a minimal scope for a simple accounting application that demonstrates core accounting flows.

**Prompt 2:**
What features are essential to show basic accounting logic without building a full system?

**Prompt 3 (refinement):**
Simplify the scope further to ensure it can be completed quickly while still being coherent.

**Outcome:**
Final scope includes:

* revenue transactions
* expense transactions
* partner tracking (customers/vendors)
* simple reporting (P&L and partner ledger)

---

## Step 3 — Designing data model

**Prompt 1:**
Suggest a minimal data model for an accounting system (transactions, journal entries, partners).

**Prompt 2:**
What is the relationship between a transaction and journal entries?

**Prompt 3:**
Provide a simple Python-friendly structure (classes or dictionaries) for storing entries.

**Prompt 4 (refinement):**
Reduce the model to the smallest possible structure while keeping consistency.

**Outcome:**
Defined core entities:

* Transaction (business event)
* JournalEntry (debit/credit lines)
* Partner (customer/vendor)

---

## Step 4 — Posting logic design

**Prompt 1:**
Explain how revenue transactions should be recorded using double-entry accounting.

**Prompt 2:**
What accounts should be affected in a system with fixed accounts (cash, receivables, revenue)?

**Prompt 3:**
Do the same for expense transactions.

**Prompt 4:**
Provide simple logic for generating balanced journal entries programmatically.

**Outcome:**
Defined consistent posting rules:

* Revenue → Debit Accounts Receivable, Credit Revenue
* Expense → Debit Expense, Credit Cash or Accounts Payable
* All entries must be balanced

---

## Step 5 — Chart of accounts

**Prompt 1:**
Suggest a minimal fixed chart of accounts for a demo accounting system.

**Prompt 2:**
Explain why a fixed chart is acceptable for a simplified application.

**Outcome:**
Used predefined accounts:

* 1000 — Cash
* 1100 — Accounts Receivable
* 2000 — Accounts Payable
* 4000 — Revenue
* 5000 — Expense

---

## Step 6 — Reporting logic

**Prompt 1:**
How to calculate a simple Profit and Loss statement from journal entries?

**Prompt 2:**
How to aggregate data for a partner ledger?

**Prompt 3:**
What is the simplest way to structure these calculations in Python?

**Prompt 4 (refinement):**
Simplify reporting logic to avoid overengineering.

**Outcome:**

* P&L = total revenue − total expenses
* Partner ledger = movements grouped by partner

---

## Step 7 — Streamlit UI design

**Prompt 1:**
Propose a minimal Streamlit UI structure for this type of application.

**Prompt 2:**
What pages or sections are enough for usability without adding complexity?

**Prompt 3:**
Provide an example layout with forms and simple navigation.

**Outcome:**
Defined UI structure:

* Create transaction
* View transactions
* Reports (P&L, Partner Ledger)

---

## Step 8 — Implementation support

**Prompt 1:**
Generate simple Python functions for creating journal entries.

**Prompt 2:**
Provide an example of storing transactions and entries in memory (or simple storage).

**Prompt 3:**
How to aggregate data for reports in a clean and readable way?

**Outcome:**
Implemented core logic with focus on clarity and separation of concerns.

---

## Step 9 — Docker setup

**Prompt 1:**
Provide a minimal Dockerfile to run a Streamlit application.

**Prompt 2:**
Explain how to build and run the container.

**Outcome:**
Created a working containerized setup for easy запуск and review.

---

## Step 10 — Final refinement

**Prompt 1:**
Review the architecture and suggest simplifications.

**Prompt 2:**
Identify unnecessary complexity and remove it.

**Outcome:**
Final solution is minimal, consistent, and focused on core accounting flow.

---

## Notes

LLM tools were used to:

* structure the development process
* validate accounting logic
* speed up implementation

All generated outputs were reviewed and adapted to ensure correctness and understanding.
