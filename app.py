import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
m_name = "Junior Olympics"
m_date = datetime(2026, 3, 20) 
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39, "50 Back": 36.29, "100 Back": 117.99, "50 Breast": 40.99, "100 Breast": 130.19, "50 Fly": 34.39, "100 Fly": 118.99, "100 IM": 118.29, "200 IM": 248.79}

if 'pbs' not in st.session_state: st.session_state['pbs'] = {e: 0.0 for e in cuts}
if 'goals' not in st.session_state: st.session_state['goals'] = {e: 0.0 for e in cuts}

# --- 2. THE CSS ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp {background-color: white !important;} .stApp p, .stApp span, .stApp label, .stApp td, .stApp th, .stApp div {color: black !important;} [data-testid='stSidebar'] {background-color: #111111 !important;} [data-testid='stSidebar'] p, [data-testid='stSidebar'] span, [data-testid='stSidebar'] label, [data-testid='stSidebar'] h2 {color: white !important;}</style>", unsafe_allow_html=True)

# Banner
header_html = "<div style='background-color:#0056b3;padding:20px;border-radius:15px;color:white;text-align:center;margin-bottom:20px;'><h1 style='color:white;margin:0;'>{} TRACKER</h1></div>".format(swimmer_name.upper())
st.markdown(header_html, unsafe_allow_html=True)

# --- 3. COUNTDOWN ---
days = (m_date - datetime.now()).days
if days >= 0:
    st.info("⏳ {} Days until {}".format(days, m_name))
else:
    st.success("🎉 {} Day!".format(m_name))

# --- 4.
