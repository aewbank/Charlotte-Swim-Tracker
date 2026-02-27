import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
m_name = "Junior Olympics"
m_date = datetime(2026, 3, 20) 
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39, "50 Back": 36.29, "100 Back": 117.99, "50 Breast": 40.99, "100 Breast": 130.19, "50 Fly": 34.39, "100 Fly": 118.99, "100 IM": 118.29, "200 IM": 248.79}

if "pb_data" not in st.session_state: st.session_state["pb_data"] = {e: 0.0 for e in cuts}
if "goal_data" not in st.session_state: st.session_state["goal_data"] = {e: 0.0 for e in cuts}

# --- 2. THE ULTIMATE VISIBILITY CSS ---
st.set_page_config(page_title="Swim Tracker", layout="centered")

st.markdown("""
    <style>
    /* Force the entire app background to white */
    .stApp {
        background-color: white !important;
    }

    /* Force the Table container to be white with black text */
    .stTable, [data-testid="stTable"] {
        background-color: white !important;
        color: black !important;
        border: 1px solid #eeeeee;
        border-radius: 10px;
    }

    /* Target every single cell in the table to be black text */
    .stTable td, .stTable th, [data-testid="stTable"] td, [data-testid="stTable"] th {
        color: black !important;
        background-color: white !important;
    }

    /* Sidebar Styling: Keep it dark so it's distinct */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Header Banner */
    .header-box {
        background-color: #0056b3;
        padding: 20px;
        border-radius: 15px;
        color: white !important;
        text-align: center;
        margin-bottom: 20px;
    }
    .header-box h1 { color: white !important; margin: 0; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)

days = (m_date - datetime.now()).days
if days >= 0:
    st.info(f"⏳ {days} Days until {m_name}")
else:
    st.success(f"🎉 {m_name} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    ev = st.selectbox("Select Event", list(cuts.keys()), key="select_event_widget")
    
    st.subheader("New PB")
    p_m = st.number_input("Min", min_value=0, step=1, value=0, key="min_input_pb")
    p_s = st.number_input("Sec", min_value=0.0, max_value=59.99, step=0.01, value=0.0, key="sec_input_pb")
    if st.button("Save PB", key="pb_button"):
        st.session_state["pb_data"][ev] = float((p_m * 60) + p_s)
        st.balloons()
    
    st.divider()
    
    st.subheader("New Goal")
    g_m = st.number_input("Min ", min_value=0, step=1, value=0, key="min_input_goal")
    g_s = st.number_input("Sec ", min_value=0.0, max
