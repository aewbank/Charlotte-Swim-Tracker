import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA ---
name = "Charlotte" 
meet = "2026 VA Age Group Champs"
m_date = datetime(2026, 3, 12) 

vsi = {
    "50 Free": 31.79, "100 Free": 69.99, "200 Free": 151.59,
    "500 Free": 403.19, "50 Back": 36.99, "100 Back": 78.99,
    "50 Breast": 41.69, "100 Breast": 91.69, "50 Fly": 35.39,
    "100 Fly": 82.59, "100 IM": 79.59, "200 IM": 171.99
}

if "pbs" not in st.session_state: st.session_state["pbs"] = {e: 0.0 for e in vsi}
if "gls" not in st.session_state: st.session_state["gls"] = {e: 0.0 for e in vsi}

# --- 2. THE CSS HAMMER (Targets EVERYTHING in the main body) ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp {background-color: white !important;} [data-testid='stMain'] * {color: black !important;} div[data-testid='stTable'] {background-color: white !important;} div[data-testid='stTable'] th, div[data-testid='stTable'] td {color: black !important; background-color: white !important;} [data-testid='stSidebar'] {background-color: #111111 !important;} [data-testid='stSidebar'] * {color: white !important;} .header-box {background-color: #0056b3; padding: 20px; border-radius: 15px; margin-bottom: 20px;} .header-box h1 {color: white !important; margin: 0; text-align: center;}</style>", unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown(f'<div class="header-box"><h1 style="color:white !important;">🏊 {name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)
days =
