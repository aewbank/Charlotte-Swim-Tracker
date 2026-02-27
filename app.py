import streamlit as st
import pandas as pd

st.set_page_config(page_title="Charlotte's Swim Tracker", layout="centered")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stHeader { background-color: #0056b3; color: white; padding: 20px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏊 Charlotte's Performance Dashboard")

# --- DATA ---
cuts = {"50 Free": 31.39, "100 Free": 109.29, "500 Free": 379.39} # Add the rest
if 'pbs' not in st.session_state:
    st.session_state.pbs = {event: 0.0 for event in cuts}

# --- SIDEBAR UPDATES ---
st.sidebar.header("Update Times")
event_to_update = st.sidebar.selectbox("Select Event", list(cuts.keys()))
new_time = st.sidebar.number_input("Enter Time (seconds)", min_value=0.0, step=0.1)
if st.sidebar.button("Update Dashboard"):
    st.session_state.pbs[event_to_update] = new_time

# --- TABLE DISPLAY ---
data = []
for event, cut in cuts.items():
    pb = st.session_state.pbs[event]
    diff = pb - cut if pb > 0 else 0
    status = "✅ ACHIEVED" if (pb > 0 and pb <= cut) else ("+" + str(round(diff, 2)) if pb > 0 else "--")
    data.append({"Event": event, "Current PB": pb, "A Cut": cut, "Status": status})

df = pd.DataFrame(data)
st.table(df)

# --- CHECKLIST ---
st.subheader("🎒 Meet Day Checklist")
col1, col2 = st.columns(2)
with col1:
    st.checkbox("2 Pairs of Goggles")
    st.checkbox("Team Cap")
with col2:
    st.checkbox("Water Bottle")
    st.checkbox("Clean Towels")
