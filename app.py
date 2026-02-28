import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & OFFICIAL 2025-2028 VSI CHAMPIONSHIP QTS ---
swimmer_name = "Charlotte" 
m_name = "2026 VA Age Group Champs"
m_date = datetime(2026, 3, 12) 

# Official 2025-2028 Virginia Swimming AGC QTs (9-10 Girls)
# Every time is converted to TOTAL SECONDS for Python stability
vsi_cuts_seconds = {
    "50 Free": 30.59, 
    "100 Free": 67.49,    # (1:07.49)
    "200 Free": 146.79,   # (2:26.79)
    "500 Free": 382.79,   # (6:22.79)
    "50 Back": 35.59, 
    "100 Back": 76.89,    # (1:16.89)
    "50 Breast": 40.09, 
    "100 Breast": 88.09,   # (1:28.09)
    "50 Fly": 34.09, 
    "100 Fly": 78.89,    # (1:18.89)
    "100 IM": 76.89,     # (1:16.89)
    "200 IM": 166.39     # (2:46.39)
}

if "pb_data" not in st.session_state: st.session_state["pb_data"] = {e: 0.0 for e in vsi_cuts_seconds}
if "goal_data" not in st.session_state: st.session_state["goal_data"] = {e: 0.0 for e in vsi_cuts_seconds}

# --- 2. THE VISIBILITY CSS ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp {background-color: white !important;} .stTable, [data-testid='stTable'] {background-color: white !important; color: black !important;} .stTable td, .stTable th {color: black !important; background-color: white !important; border: 1px solid #f0f0f0 !important;} [data-testid='stSidebar'] {background-color: #111111 !important;} [data-testid='stSidebar'] * {color: white !important;} .header-box {background-color: #0056b3; padding: 20px; border-radius: 15px; color: white !important; text-align: center; margin-bottom: 20px;} .header-box h1 {color: white !important; margin: 0;}</style>", unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)
days = (m_date - datetime.now()).days
if days >= 0: st.info(f"⏳ {days} Days until {m_name}")
else: st.success(f"🎉 {m_name} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    ev = st.selectbox("Select Event", list(vsi_cuts_seconds.keys()), key="sel_ev")
    
    st.subheader("New PB")
    p_m = st.number_input("Min", min_value=0, step=1, value=0, key="in_p_m")
    p_s = st.number_input("Sec", min_value=0.0, max_value=59.99, step=0.01, value=0.0, key="in_p_s")
    if st.button("Save PB", key="btn_p"):
        st.session_state["pb_data"][ev] = float((p_m * 60) + p_s)
        st.balloons()
    
    st.divider()
    
    st.subheader("New Goal")
    g_m = st.number_input("Min Goal", min_value=0, step=1, value=0, key="in_g_m")
    g_s = st.number_input("Sec Goal", min_value=0.0, max_value=59.99, step=0.01, value=0.0, key="in_
