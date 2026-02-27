import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA & CONFIG ---
swimmer_name = "Charlotte" 
m_name = "Junior Olympics"
m_date = datetime(2026, 3, 20) 
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39, "50 Back": 36.29, "100 Back": 117.99, "50 Breast": 40.99, "100 Breast": 130.19, "50 Fly": 34.39, "100 Fly": 118.99, "100 IM": 118.29, "200 IM": 248.79}

# FIXED: Renamed state keys to 'pb_data' and 'goal_data' to avoid widget conflicts
if "pb_data" not in st.session_state: st.session_state["pb_data"] = {e: 0.0 for e in cuts}
if "goal_data" not in st.session_state: st.session_state["goal_data"] = {e: 0.0 for e in cuts}

# --- 2. STYLE & HEADER ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.header {background:#0056b3; padding:20px; border-radius:10px; color:white; text-align:center; margin-bottom:20px;} .stTable td {color:black !important;}</style>", unsafe_allow_html=True)
st.markdown(f"<div class='header'><h1>🏊 {swimmer_name.upper()} TRACKER</h1></div>", unsafe_allow_html=True)

# Countdown
days = (m_date - datetime.now()).days
if days >= 0: st.info(f"⏳ {days} Days until {m_name}")
else: st.success(f"🎉 {m_name} Day!")

# --- 3. SIDEBAR ---
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
    g_s = st.number_input("Sec ", min_value=0.0, max_value=59.99, step=0.01, value=0.0, key="sec_input_goal")
    if st.button("Save Goal", key="goal_button"):
        st.session_state["goal_data"][ev] = float((g_m * 60) + g_s)
        st.toast("Goal Saved!")

# --- 4. TABLE LOGIC ---
def fmt(s):
    try:
        s = float(s)
        if s <= 0: return "--"
        if s < 60: return "{:.2f}s".format(s)
        return "{:d}:{:05.2f}".format(int(s//60), s%60)
    except: return "--"

rows = []
for e, c in cuts.items():
    p = float(st.session_state["pb_data"].get(e, 0.0))
    g = float(st.session_state["goal_data"].get(e, 0.0))
    
    if p <= 0: stat = "No Time"
    elif p <= c: stat = "✅ ACHIEVED"
    else: stat = "{:.2f}s to go".format(p - c)
    
    rows.append({"Event": e, "Current PB": fmt(p), "Goal": fmt(g), "A Cut": fmt(c), "Status": stat})

st.subheader("Performance Overview")
st.table(pd.DataFrame(rows))

# --- 5. FOOTER ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("🎒 Checklist")
    st.checkbox("2 Pairs Goggles", key="check_goggles")
    st.checkbox("Team Cap", key="check_cap")
with c2:
    st.subheader("🍌 Nutrition")
    st.warning("Eat oatmeal or a banana 2 hours before warm-ups!")
