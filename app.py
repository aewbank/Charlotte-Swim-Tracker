import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
meet_name = "Junior Olympics"
meet_date = datetime(2026, 3, 20) 

# Full 9-10 Girls USA Swimming 'A' Cuts
cuts = {
    "50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39,
    "50 Back": 36.29, "100 Back": 117.99,
    "50 Breast": 40.99, "100 Breast": 130.19,
    "50 Fly": 34.39, "100 Fly": 118.99,
    "100 IM": 118.29, "200 IM": 248.79
}

# --- 2. STATE INITIALIZATION ---
# QA Note: Initializing state outside of logic to prevent KeyErrors
if 'pbs' not in st.session_state:
    st.session_state['pbs'] = {event: 0.0 for event in cuts}
if 'goals' not in st.session_state:
    st.session_state['goals'] = {event: 0.0 for event in cuts}

# --- 3. UI & STYLING ---
st.set_page_config(page_title="Swim Tracker", layout="centered")

# Forced Contrast CSS
# QA Note: Using a raw string (r"") to prevent escaping issues in CSS
st.markdown(r"""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    [data-testid="stHeader"] { background-color: rgba(0,0,0,0) !important; }
    
    /* Main Content Colors */
    .stApp p, .stApp span, .stApp label, .stApp td, .stApp th, .stApp div {
        color: #000000 !important;
    }

    /* Sidebar Contrast */
    [data-testid="stSidebar"] { background-color: #111111 !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] h2 {
        color: #FFFFFF !important;
    }

    /* Banner */
    .header-box {
        background-color: #0056b3;
        padding: 20px;
        border-radius: 15px;
        color: #FFFFFF !important;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-box h1 { color: #FFFFFF !important;
