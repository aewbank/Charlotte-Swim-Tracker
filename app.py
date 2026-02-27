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

# --- 2. FORCED VISIBILITY STYLING ---
st.set_page_config(page_title=f"{swimmer_name}'s Tracker", layout="centered")

st.markdown("""
    <style>
    /* Force all main text to be Black */
    root, .stApp, p, span, label, .stMarkdown {
        color: #000000 !important;
    }
    
    /* Header Box Styling */
    .header-box {
        background-color: #0056b3;
        padding: 25px;
        border-radius: 15px;
        color: #ffffff !important; /* Keep header text white */
        text-align: center;
        margin-bottom: 20px;
    }
    .header-box h1 {
        color: #ffffff !important;
    }

    /* Table Styling */
    .stTable {
        background-color: #ffffff;
        border: 1px solid #dddddd;
        border-radius: 10px;
    }
    
    /* Sidebar Text Force Black */
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label {
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()}\'S TRACKER</h1></div>', unsafe_allow_html=True)

days_left = (meet_date - datetime.now()).days
if days_left >= 0:
    st.info(f"⏳ **{days_left} Days** until {meet_name}!")
else:
    st.success(f"🎉 It's {meet_name} Day! Go {swimmer_name}!")

# --- 4. SIDEBAR INPUT ---
with st.sidebar:
    st.header("⏱ Update Times")
    event_choice = st.selectbox("Select Event", list(cuts.keys()))
    st.write("Enter total seconds (Ex: 1:15.50 = 75.50)")
    updated_time = st.number_input("New PB (Seconds)", min_value=0.0, format="%.2f")
    
    if st.button("Update Dashboard"):
        st.session_state.pbs[event_choice] = updated_time
        st.balloons()

# --- 5. DASHBOARD TABLE ---
def format_time(seconds):
    if seconds == 0: return "--"
    if seconds < 60: return f"{seconds:.
