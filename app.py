import streamlit as st
from groq import Groq
from datetime import datetime
import pandas as pd
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Page config
st.set_page_config(page_title="Smart AI Budget", page_icon="💰", layout="wide")

st.title("💰 Smart AI Budget Assistant")

# ---------------- API KEY ----------------
def get_api_key():
    return st.session_state.get("api_key") or os.getenv("GROQ_API_KEY")

# ---------------- GROQ ----------------
def call_groq_api(prompt, api_key):
    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial advisor. Always respond using INR (₹) currency only. Never use $ symbol."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1000
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

# ---------------- MAIN ----------------
def main():

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")

        key_input = st.text_input("Enter Groq API Key (optional)", type="password")

        if key_input:
            st.session_state.api_key = key_input

        if os.getenv("GROQ_API_KEY"):
            st.success("Using .env API key")
        else:
            st.warning("Enter API key manually")

    api_key = get_api_key()

    if not api_key:
        st.error("Please provide API key")
        return

    # Service selection
    service = st.selectbox("Select Service", [
        "Budget Analysis",
        "Expense Tracking",
        "File Upload Analysis"
    ])

    # ---------------- BUDGET ----------------
    if service == "Budget Analysis":

        income = st.number_input("Salary per Annum (₹)", value=300000)
        expenses = st.number_input("Expenses per month (₹)", value=2000)

        if st.button("Analyze"):

            yearly_expenses = expenses * 12
            remaining = income - yearly_expenses

            prompt = f"""
            Analyze this financial data (all values in INR ₹):

            Salary per Annum: ₹{income}
            Monthly Expenses: ₹{expenses}
            Yearly Expenses: ₹{yearly_expenses}
            Yearly Remaining: ₹{remaining}

            Provide practical budget advice.
            Use INR (₹) only.
            """

            result = call_groq_api(prompt, api_key)
            st.subheader("📊 AI Advice")
            st.write(result)

    # ---------------- EXPENSE TRACKING ----------------
    elif service == "Expense Tracking":

        category = st.selectbox("Category", ["Food", "Shopping", "Travel"])
        amount = st.number_input("Amount (₹)", value=50)
        desc = st.text_input("Description")

        if st.button("Add Expense"):

            if "expenses" not in st.session_state:
                st.session_state.expenses = []

            st.session_state.expenses.append({
                "category": category,
                "amount": amount,
                "desc": desc,
                "date": datetime.now().strftime("%Y-%m-%d")
            })

            st.success("Expense Added")

        if "expenses" in st.session_state:
            st.subheader("📋 Expenses")

            total = sum(x["amount"] for x in st.session_state.expenses)
            st.write(f"Total Spent: ₹{total}")

            st.write(st.session_state.expenses)

            if st.button("Analyze Expenses"):
                prompt = f"""
                Analyze these expenses (in INR ₹):
                {st.session_state.expenses}

                Provide insights and saving tips.
                Use ₹ only.
                """

                result = call_groq_api(prompt, api_key)
                st.write(result)

    # ---------------- FILE UPLOAD ----------------
    elif service == "File Upload Analysis":

        file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

        if file:

            if file.name.endswith(".csv"):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)

            st.subheader("📊 Data Preview")
            st.dataframe(df.head())

            # Convert amount column to ₹ display if exists
            amount_cols = [col for col in df.columns if "amount" in col.lower()]
            if amount_cols:
                col = amount_cols[0]
                try:
                    total_amount = df[col].sum()
                    st.write(f"Total Amount: ₹{total_amount}")
                except:
                    pass

            if st.button("Analyze File"):
                prompt = f"""
                Analyze this financial dataset (values in INR ₹):

                {df.head().to_string()}

                Provide insights and recommendations.
                Use ₹ only.
                """

                result = call_groq_api(prompt, api_key)
                st.write(result)

# ---------------- RUN ----------------
if __name__ == "__main__":
    main()