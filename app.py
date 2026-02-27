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

# --- 2. STATE INITIALIZATION ---
if 'pbs' not in st.session_state:
    st.session_state['pbs'] = {event: 0.0 for event in cuts}
if 'goals' not in st.session_state:
    st.session_state['goals'] = {event: 0.0 for event in cuts}

# --- 3. UI & STYLING (FIXED) ---
st.set_page_config(page_title="Swim Tracker", layout="centered")

# Using single-line style strings to prevent "Unterminated Literal" errors
st.markdown("<style>.stApp { background-color: #FFFFFF !important; }</style>", unsafe_allow_html=True)
st.markdown("<style>.stApp p, .stApp span, .stApp label, .stApp td, .stApp th, .stApp div { color: #000000 !important; }</style>", unsafe_allow_html=True)
st.markdown("<style>[data-testid='stSidebar'] { background-color: #111111 !important; }</style>", unsafe_allow_html=True)
st.markdown("<style>[data-testid='stSidebar'] p, [data-testid='stSidebar'] span, [data-testid='stSidebar'] label, [data-testid='stSidebar'] h2 { color: #FFFFFF !important; }</style>", unsafe_allow_html=True)

# Banner Styling
banner_html = f"<div style='background-color: #0056b3; padding: 20px; border-radius: 15px; color: #FFFFFF; text-align: center; margin-bottom: 20px;'><h1 style='color: #FFFFFF; margin: 0;'>🏊 {swimmer_name.upper()}</h1></div>"
st.markdown(banner_html, unsafe_allow_html=True)

# --- 4. TOP DISPLAY ---
days_left = (meet_date - datetime.now()).days
if days_left >= 0:
    st.info(f
