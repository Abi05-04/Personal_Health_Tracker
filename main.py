import streamlit as st
import pandas as pd
import openpyxl
from datetime import datetime

from database import *

# ---------------- INIT ----------------
st.set_page_config(page_title="Health Tracker", layout="wide")
create_table()

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.session_state.user == "admin" and st.session_state.passw == "1234":
        st.session_state.logged_in = True
    else:
        st.error("❌ Invalid credentials")

# ---------------- LOGIN UI ----------------
if not st.session_state.logged_in:
    st.title("🔐 Login")

    st.text_input("Username", key="user")
    st.text_input("Password", type="password", key="passw")

    st.button("Login", on_click=login)
    st.stop()

# ---------------- MAIN APP ----------------
st.title("🏥 Health Tracker Dashboard")

# ---------------- ADD DATA ----------------
with st.sidebar:
    st.header("➕ Add Health Data")

    date = st.date_input("Date")
    weight = st.number_input("Weight (kg)")
    calories = st.number_input("Calories")
    steps = st.number_input("Steps")
    water = st.number_input("Water (ml)")

    if st.button("Add Entry"):
        add_entry(str(date), weight, calories, steps, water)
        st.success("✅ Data Added")

# ---------------- LOAD DATA ----------------
entries = get_entries()

if entries:
    df = pd.DataFrame(entries, columns=["ID", "Date", "Weight", "Calories", "Steps", "Water"])

    latest = df.iloc[-1]

    # ---------------- DASHBOARD CARDS ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("⚖️ Weight", f"{latest['Weight']} kg")
    col2.metric("🔥 Calories", latest["Calories"])
    col3.metric("🏃 Steps", latest["Steps"])
    col4.metric("💧 Water", f"{latest['Water']} ml")

    # ---------------- TABLE ----------------
    st.subheader("📄 All Records")
    st.dataframe(df)

    # ---------------- DELETE ----------------
    delete_id = st.number_input("Enter ID to Delete", step=1)
    if st.button("Delete Entry"):
        delete_entry(int(delete_id))
        st.success("🗑 Entry Deleted")

    # ---------------- CHARTS ----------------
    st.subheader("📊 Charts")

    st.line_chart(df.set_index("Date")["Weight"])
    st.bar_chart(df.set_index("Date")["Steps"])

    # ---------------- EXPORT ----------------
    if st.button("Export to Excel"):
        file = "health_data.xlsx"
        df.to_excel(file, index=False)
        with open(file, "rb") as f:
            st.download_button("Download File", f, file)

else:
    st.info("No data yet. Add entries from sidebar.")

# ---------------- LOGOUT ----------------
if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    st.rerun()