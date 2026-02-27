import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
m_name = "Junior Olympics"import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
m_name = "Junior Olympics"
m_date = datetime(2026, 3, 20) 
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39, "50 Back": 36.29, "100 Back": 117.99, "50 Breast": 40.99, "100 Breast": 130.19, "50 Fly": 34.39, "100 Fly": 118.99, "100 IM": 118.29, "200 IM": 248.79}

if 'pbs' not in st.session_state: st.session_state['pbs'] = {e: 0.0 for e in cuts}
if 'goals' not in st.session_state: st.session_state['goals'] = {e: 0.0 for e in cuts}

# --- 2. UI STYLING ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp { background-color: white; } .header-box { background-color: #0056b3; padding: 20px; border-radius: 10px; color: white; text-align: center; margin-bottom: 20px; } .stTable td { color: black !important; }</style>", unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)
days = (m_date - datetime.now()).days
if days >= 0: st.info(f"⏳ {days} Days until {m_name}")
else: st.success(f"🎉 {m_name} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    ev = st.selectbox("Select Event", list(cuts.keys()), key="ev_key")
    
    st.subheader("New PB")
    c_pb1, c_pb2 = st.columns(2)
    with c_pb1: pb_m = st.number_input("Min", min_value=0, step=1, key="pbm")
    with c_pb2: pb_s = st.number_input("Sec", min_value=0.0, max_value=59.99, step=0.01, key="pbs")
    if st.button("Save PB", key="pbtn"):
        st.session_state['pbs'][ev] = (pb_m * 60) + pb_s
        st.balloons()
    
    st.divider()
    
    st.subheader("New Goal")
    c_gl1, c_gl2 = st.columns(2)
    with c_gl1: gl_m = st.number_input("Min", min_value=0, step=1, key="glm")
    with c_gl2: gl_s = st.number_input("Sec", min_value=0.0, max_value=59.99, step=0.01, key="gls")
    if st.button("Save Goal", key="gbtn"):
        st.session_state['goals'][ev] = (gl_m * 60) + gl_s
        st.toast("Goal Saved!")

# --- 5. TABLE LOGIC ---
def fmt(s):
    if s <= 0: return "--"
    if s < 60: return "{:.2f}s".format(s)
    return "{:d}:{:05.2f}".format(int(s//60), s%60)

rows = []
for e, c in cuts.items():
    p = st.session_state['
m_date = datetime(2026, 3, 20) 
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39, "50 Back": 36.29, "100 Back": 117.99, "50 Breast": 40.99, "100 Breast": 130.19, "50 Fly": 34.39, "100 Fly": 118.99, "100 IM": 118.29, "200 IM": 248.79}

if 'pbs' not in st.session_state:
    st.session_state['pbs'] = {e: 0.0 for e in cuts}
if 'goals' not in st.session_state:
    st.session_state['goals'] = {e: 0.0 for e in cuts}

# --- 2. CLEANER UI STYLING ---
st.set_page_config(page_title="Swim Tracker", layout="centered")

# We are using 'st.markdown' with simpler CSS that won't hide the sidebar
st.markdown("""
    <style>
    /* Force a clean light theme */
    .main { background-color: #f9f9f9; }
    
    /* Style the header banner */
    .header-box {
        background-color: #0056b3;
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Make the table text stand out */
    .stTable td { color: black !important; font-weight: 500; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)

days = (m_date - datetime.now()).days
if days >= 0:
    st.info(f"⏳ {days} Days until {m_name}")
else:
    st.success(f"🎉 {m_name} Day!")

# --- 4. SIDEBAR (SPLIT-TIME INPUTS) ---
with st.sidebar:
    st.header("Update Times")
    ev = st.selectbox("Select Event", list(cuts.keys()), key="ev_key")
    
    st.subheader("New PB")
    c_pb1, c_pb2 = st.columns(2)
    with c_pb1: pb_m = st.number_input("Min", min_value=0, step=1, key="pbm")
    with c_pb2: pb_s = st.number_input("Sec", min_value=0.0, max_value=59.99, step=0.01, key="pbs")
    
    if st
