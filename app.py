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

# Initialize session memory for PBs and Goals
if 'pbs' not in st.session_state:
    st.session_state.pbs = {event: 0.0 for event in cuts}
if 'goals' not in st.session_state:
    st.session_state.goals = {event: 0.0 for event in cuts}

# --- 2. HIGH-VISIBILITY STYLING ---
st.set_page_config(page_title=f"{swimmer_name}'s Tracker", layout="centered")

st.markdown("""
    <style>
    root, .stApp, p, span, label, .stMarkdown, td, th {
        color: #000000 !important;
    }
    .header-box {
        background-color: #0056b3;
        padding: 25px;
        border-radius: 15px;
        color: #ffffff !important;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-box h1 { color: #ffffff !important; }
    .stTable {
        background-color: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 10px;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_
