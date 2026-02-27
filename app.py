import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Charlotte's Swim Tracker", layout="centered")

# Custom Styling for the Blue Banner and clean look
st.markdown("""
    <style>
    .stApp { background-color: white; }
    .header-box {
        background-color: #0056b3;
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FULL DATA SET ---
# All 9-10 Girls USA Swimming 'A' Cuts
cuts = {
    "50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39,
    "50 Back": 36.29, "100 Back": 117.99,
    "50 Breast": 40.99, "100 Breast": 130.19,
    "50 Fly": 34.39, "100 Fly": 118.99,
    "100 IM": 118.29, "200 IM": 248.79
}

# Persistent memory for the current session
if 'pbs' not in st.session_state:
    st.session_state.pbs = {event: 0.0 for event in cuts}

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()}\'S TRACKER</h1></div>', unsafe_allow_html=True)

meet_date = datetime(2026, 3, 20)
days_left = (meet_date - datetime.now()).days
if days_left >= 0:
    st.info(f"⏳ **{days_left} Days** until Junior Olympics!")
else:
    st.success("🎉 It's Meet Day! Good luck Charlotte!")

# --- 4. UPDATE SIDEBAR ---
with st.sidebar:
    st.header("⏱ Update Times")
    event_choice = st.selectbox("Select Event", list(cuts.keys()))
    
    # Help user with format
    st.write("Enter as total seconds (e.g., 1:12.20 = 72.2)")
    updated_time = st.number_input("New PB (Seconds)", min_value=0.0, format="%.2f")
    
    if st.button("Save New Time"):
        st.session_state.pbs[event_choice] = updated_time
        st.balloons() # Fun celebration!

# --- 5. DATA LOGIC & TABLE ---
def format_time(seconds):
    if seconds == 0: return "--"
    if seconds < 60: return f"{seconds:.2f}s"
    return f"{int(seconds//60)}:{seconds%60:05.2f}"

display_data = []
for event, cut in cuts.items():
    pb = st.session_state.pbs[event]
    
    if pb == 0:
        status = "N/A"
    elif pb <= cut:
        status = "✅ ACHIEVED"
    else:
        gap = pb - cut
        status = f"-{gap:.2f}s to go"
    
    display_data.append({
        "Event": event,
        "Current PB": format_time(pb),
        "A Cut": format_time(cut),
        "Status": status
    })

# Render the Table
st.table(pd.DataFrame(display_data))

# --- 6. EXTRAS ---
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎒 Checklist")
    st.checkbox("2 Pairs Goggles")
    st.checkbox("Team Cap")
    st.checkbox("2 Towels")
    st.checkbox("Water Bottle")

with col2:
    st.subheader("🍌 Nutrition Tip")
    st.write("*Eat oatmeal or a banana 2 hours before warm-ups. Avoid heavy fats!*")
    st.caption("Quote of the day: 'Hard work beats talent when talent doesn't work hard.'")
