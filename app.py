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

# Session memory
if 'pbs' not in st.session_state:
    st.session_state.pbs = {event: 0.0 for event in cuts}
if 'goals' not in st.session_state:
    st.session_state.goals = {event: 0.0 for event in cuts}

# --- 2. STYLING ---
st.set_page_config(page_title="Swim Tracker", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: white; }
    p, span, label, td, th, div { color: black !important; }
    .header-box {
        background-color: #0056b3;
        padding: 20px;
        border-radius: 15px;
        color: white !important;
        text-align: center;
    }
    .header-box h1 { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()}</h1></div>', unsafe_allow_html=True)

days_left = (meet_date - datetime.now()).days
if days_left >= 0:
    st.info(f"⏳ {days_left} Days until {meet_name}")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Times")
    event_choice = st.selectbox("Select Event", list(cuts.keys()))
    
    val_pb = st.number_input("New PB (Seconds)", min_value=0.0, format="%.2f", key="pb_input")
    if st.button("Save PB"):
        st.session_state.pbs[event_choice] = val_pb
        st.balloons()
            
    val_goal = st.number_input("Goal (Seconds)", min_value=0.0, format="%.2f", key="goal_input")
    if st.button("Save Goal"):
        st.session_state.goals[event_choice] = val_goal
        st.success("Goal Saved!")

# --- 5. DATA TABLE ---
def format_time(seconds):
    if seconds <= 0: return "--"
    if seconds < 60: return f"{seconds:.2f}s"
    m = int(seconds // 60)
    s = seconds % 60
    return f"{m}:{s:05.2f}"

rows = []
for event, cut in cuts.items():
    pb = st.session_state.pbs[event]
    goal = st.session_state.goals[event]
