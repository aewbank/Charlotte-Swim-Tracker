import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
meet_name = "Junior Olympics"
meet_date = datetime(2026, 3, 20) 

cuts = {
    "50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39,
    "50 Back": 36.29, "100 Back": 117.99,
    "50 Breast": 40.99, "100 Breast": 130.19,
    "50 Fly": 34.39, "100 Fly": 118.99,
    "100 IM": 118.29, "200 IM": 248.79
}

# Session memory (Resets on refresh until we connect Google Sheets)
if 'pbs' not in st.session_state:
    st.session_state.pbs = {event: 0.0 for event in cuts}
if 'goals' not in st.session_state:
    st.session_state.goals = {event: 0.0 for event in cuts}

# --- 2. STYLING (Forced Black Text) ---
st.set_page_config(page_title=f"{swimmer_name}'s Tracker", layout="centered")

# This block forces the browser to show black text on a white background
st.markdown(
    """
    <style>
    .stApp { background-color: #ffffff; }
    root, p, span, label, td, th, .stMarkdown { color: #000000 !important; }
    .header-box {
        background-color: #0056b3;
        padding: 20px;
        border-radius: 15px;
        color: #ffffff !important;
        text-align: center;
    }
    .header-box h1 { color: #ffffff !important; }
    </style>
    """, 
    unsafe_allow_html=True
)

# --- 3. HEADER ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()}\'S TRACKER</h1></div>', unsafe_allow_html=True)

days_left = (meet_date - datetime.now()).days
if days_left >= 0:
    st.info(f"⏳ **{days_left} Days** until {meet_name}!")
else:
    st.success(f"🎉 It's {meet_name} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("⏱ Update Data")
    event_choice = st.selectbox("Select Event", list(cuts.keys()))
    
    # Update PB
    new_pb = st.number_input("New PB (Seconds)", min_value=0.0, format="%.2f", key="pb_val")
    if st.button("
