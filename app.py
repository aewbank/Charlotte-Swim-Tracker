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

# --- 2. THE CSS (Single Line Only) ---
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

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    ev = st.selectbox("Select Event", list(cuts.keys()), key="ev_key")
    p_val = st.number_input("New PB (Seconds)", min_value=0.0, format="%.2f", key="p_key")
    if st.button("Save PB", key="p_btn"):
        st.session_state['pbs'][ev] = p_val
        st.balloons()
    g_val = st.number_input("Goal (Seconds)", min_value=0.0, format="%.2f", key="g_key")
    if st.button("Save Goal", key="g_btn"):
        st.session_state['goals'][ev] = g_val
        st.toast("Goal Saved!")

# --- 5. TABLE LOGIC ---
def fmt(s):
    if s <= 0: return "--"
    if s < 60: return "{:.2f}s".format(s)
    return "{:d}:{:05.2f}".format(int(s//60), s%60)

rows = []
for e, c in cuts.items():
    p = st.session_state['pbs'][e]
    g = st.session_state['goals'][e]
    stat = "No Time"
    if p > 0:
        if p <= c: stat = "✅ ACHIEVED"
        else: stat = "{:.2f}s to go".format(p - c)
    rows.append({"Event": e, "Current PB": fmt(p), "Goal": fmt(g), "A Cut": fmt(c), "Status": stat})

st.table(pd.DataFrame(rows))

# --- 6. FOOTER ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("🎒 Checklist")
    st.checkbox("2 Pairs Goggles", key="k1"); st.checkbox("Team Cap", key="k2"); st.checkbox("Water Bottle", key="k3")
with c2:
    st.subheader("🍌 Nutrition")
    st.warning("Eat oatmeal or a banana 2 hours before warm-ups!")
