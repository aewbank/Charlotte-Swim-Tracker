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

if 'pbs' not in st.session_state:
    st.session_state.pbs = {event: 0.0 for event in cuts}
if 'goals' not in st.session_state:
    st.session_state.goals = {event: 0.0 for event in cuts}

# --- 2. THE ULTIMATE VISUAL FIX ---
st.set_page_config(page_title="Swim Tracker", layout="centered")

st.markdown("""
    <style>
    /* 1. MAIN BODY: Force White Background and Black Text */
    .stApp {
        background-color: #FFFFFF !important;
    }
    .stApp p, .stApp span, .stApp label, .stApp td, .stApp th, .stApp div {
        color: #000000 !important;
    }

    /* 2. SIDEBAR: Force Dark Background and White Text */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2 {
        color: #FFFFFF !important;
    }

    /* 3. HEADER BANNER: Keep Blue with White Text */
    .header-box {
        background-color: #0056b3;
        padding: 20px;
        border-radius: 15px;
        color: #FFFFFF !important;
        text-align: center;
        margin-bottom: 10px;
    }
    .header-box h1 {
        color: #FFFFFF !important;
        margin: 0;
    }

    /* 4. TABLE: Ensure borders are visible and text is sharp */
    .stTable {
        background-color: #FFFFFF !important;
        border: 1px solid #CCCCCC !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()}</h1></div>', unsafe_allow_html=True)

days_left = (meet_date
