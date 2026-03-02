import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. DATA ---
name = "Charlotte" 
meet = "2026 VA Age Group Champs"
m_dt = datetime(2026, 3, 12) 

vsi = {
    "50 Free": 31.79, "100 Free": 69.99, "200 Free": 151.59,
    "500 Free": 403.19, "50 Back": 36.99, "100 Back": 78.99,
    "50 Breast": 41.69, "100 Breast": 91.69, "50 Fly": 35.39,
    "100 Fly": 82.59, "100 IM": 79.59, "200 IM": 171.99
}

if "pbs" not in st.session_state: st.session_state["pbs"] = {e: 0.0 for e in vsi}
if "gls" not in st.session_state: st.session_state["gls"] = {e: 0.0 for e in vsi}

# --- 2. THE CSS (Forces ALL text in main body to Black) ---
st.set_page_config(page_title="Swim Tracker", layout="centered")
st.markdown("<style>.stApp {background-color: white !important;} [data-testid='stMain'] * {color: black !important;} div[data-testid='stTable'] th, div[data-testid='stTable'] td {color: black !important; background-color: white !important;} [data-testid='stSidebar'] {background-color: #111111 !important;} [data-testid='stSidebar'] * {color: white !important;} .header-box {background-color: #0056b3; padding: 20px; border-radius: 15px; margin-bottom: 20px;} .header-box h1 {color: white !important; margin: 0; text-align: center;}</style>", unsafe_allow_html=True)

# --- 3. HEADER & COUNTDOWN ---
st.markdown(f'<div class="header-box"><h1 style="color:white !important;">🏊 {name.upper()} TRACKER</h1></div>', unsafe_allow_html=True)

# Calculation kept on one short line to prevent clipping
diff = (m_dt - datetime.now()).days
if diff >= 0: st.info(f"⏳ {diff} Days until {meet}")
else: st.success(f"🎉 {meet} Day!")

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Update Performance")
    ev = st.selectbox("Event", list(vsi.keys()), key="ev_k")
    st.subheader("New PB")
    p_m = st.number_input("Min", min_value=0, step=1, key="pm")
    p_s = st.number_input("Sec", min_value=0.0, max_value=59.99, key="ps")
    if st.button("Save PB", key="pb_b"):
        st.session_state["pbs"][ev] = float((p_m * 60) + p_s)
        st.balloons()
    st.divider()
    st.subheader("New Goal")
    g_m = st.number_input("Min ", min_value=0, step=1, key="gm")
    g_s = st.number_input("Sec ", min_value=0.0, max_value=59.99, key="gs")
    if st.button("Save Goal", key="gl_b"):
        st.session_state["gls"][ev] = float((g_m * 60) + g_s)
        st.toast("Goal Saved!")

# --- 5. TABLE LOGIC ---
def fmt(s):
    try:
        v = float(s)
        if v <= 0: return "--"
        if v < 60: return "{:.2f}s".format(v)
        return "{:d}:{:05.2f}".format(int(v // 60), v % 60)
    except: return "--"

rows = []
for e, c in vsi.items():
    p = float(st.session_state["pbs"].get(e, 0.0))
    g = float(st.session_state["gls"].get(e, 0.0))
    if p <= 0: stt = "No Time"
    elif p <= c: stt = "✅ CHAMPS CUT!"
    else: stt = "{:.2f}s to go".format(p - c)
    rows.append({"Event": e, "PB": fmt(p), "Goal": fmt(g), "VSI QT": fmt(c), "Status": stt})

# Subheader (now forced black by CSS)
st.subheader("VA Age Group Champs: 10 & Under Girls")
st.table(pd.DataFrame(rows))

# --- 6. FOOTER ---
st.divider()
c1, c2 = st.columns(2)
with c1:
    st.subheader("🎒 Checklist")
    st.checkbox("2 Pairs Goggles", key="ck1")
    st.checkbox("Team Cap", key="ck2")
with c2:
    st.subheader("🍌 Nutrition")
    st.warning("Eat oatmeal or a banana 2 hours before warm-ups!")
