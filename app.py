import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
meet_name = "Junior Olympics"
meet_date = datetime(2026, 3, 20) 
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39, "50 Back": 36.29, "100 Back": 117.99, "50 Breast": 40.99, "100 Breast": 130.19, "50 Fly": 34.39, "100 Fly": 118.99, "100 IM": 118.29, "200 IM": 248.79}

if 'pbs' not in st.session_state: st.session_state['pbs'] = {e: 0.0 for e in cuts}
if 'goals' not in st.session_state: st.session_state['goals'] = {e: 0.0 for e in cuts}

# --- 2. UI & STYLING (Forced Contrast) ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp {background-color: #FFFFFF !important;} .stApp p, .stApp span, .stApp label, .stApp td, .stApp th, .stApp div {color: #000000 !important;} [data-testid='stSidebar'] {background-color: #111111 !important;} [data-testid='stSidebar'] p, [data-testid='stSidebar'] span, [data-testid='stSidebar'] label, [data-testid='stSidebar'] h2 {color: #FFFFFF !important;}</style>", unsafe_allow_html=True)

# Banner
st.markdown(f"<div style='background-color: #0056b3; padding: 20px; border-radius: 15px; color: #FFFFFF; text-align: center; margin-bottom: 20px;'><h1 style='color: #FFFFFF; margin: 0;'>🏊 {swimmer_name.upper()}</h1></div>", unsafe_allow_html=True)

# --- 3. COUNTDOWN ---
days = (meet_date - datetime.now()).days
if days >= 0: st.info(f"⏳ {days} Days until {meet_name}")
else: st.success(f"🎉 {meet_name} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    event = st.selectbox("Select Event", list(cuts.keys()), key="evt")
    v_pb = st.number_input("New PB (Seconds)", min_value=0.0, format="%.2f", key="pb_v")
    if st.button("Save PB", key="pb_b"):
        st.session_state['pbs'][event] = v_pb
        st.balloons()
    v_gl = st.number_input("Goal (Seconds)", min_value=0.0, format="%.2f", key="gl_v")
    if st.button("Save Goal", key="gl_b"):
        st.session_state['goals'][event] = v_gl
        st.toast("Goal Saved!")

# --- 5. TABLE LOGIC ---
def fmt(s):
    if s <= 0: return "--"
    if s < 60: return f"{
