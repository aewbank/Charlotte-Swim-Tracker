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

# --- 2. THE VISIBILITY CSS ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp {background-color: white !important;} .stTable, [data-testid='stTable'] {background-color: white !important; color: black !important;} .stTable td, .stTable th {color: black !important; background-color: white !important;} [data-testid='stSidebar'] {background-color: #111111 !important;} [data-testid='stSidebar'] * {color: white !important;} .header-box {background-color: #0056b3; padding: 20px; border-radius: 15px; color: white !important; text-align: center; margin-bottom: 20px;} .header-box h1 {color: white !important; margin: 0;}</style>", unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1>🏊 {swimmer_name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)
days = (m_date - datetime.now()).days
if days >= 0: st.info(f"⏳ {days} Days until {m_name}")
else: st.success(f"🎉 {m_name} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    ev = st.selectbox("Select Event", list(cuts.keys()), key="sel_ev")
    
    st.subheader("New PB")
    p_m = st.number_input("Min", min_value=0, step=1, value=0, key="in_p_m")
    p_s = st.number_input("Sec", min_value=0.0, max_value=59.99, step=0.01, value=0.0, key="in_p_s")
    if st.button("Save PB", key="btn_p"):
        st.session_state["pb_data"][ev] = float((p_m * 60) + p_s)
        st.balloons()
    
    st.divider()
    
    st.subheader("New Goal")
    g_m = st.number_input("Min Goal", min_value=0, step=1, value=0, key="in_g_m")
    g_s = st.number_input("Sec Goal", min_value=0.0, max_value=59.99, step=0.01, value=0.0, key="in_g_s")
    if st.button("Save Goal", key="btn_g"):
        st.session_state["goal_data"][ev] = float((g_m * 60) + g_s)
        st.toast("Goal Saved!")

# --- 5. TABLE LOGIC ---
def fmt(s):
    try:
        if float(s) <= 0: return "--"
        if float(s) < 60: return "{:.2f}s".format(float(s))
        return "{:d}:{:05.2f}".format(int(float(s)//60), float(s)%60)
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

# --- 6. FOOTER ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("🎒 Checklist")
    st.checkbox("2 Pairs Goggles", key="ck1"); st.checkbox("Team Cap", key="ck2")
with c2:
    st.subheader("🍌 Nutrition")
    st.warning("Eat oatmeal or a banana 2 hours before warm-ups!")
