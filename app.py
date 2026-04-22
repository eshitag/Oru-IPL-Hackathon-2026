import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

# 1. SETUP & THEME
st.set_page_config(page_title="IPL Tactical Commander", page_icon="🏏", layout="wide")

# Custom CSS for a high-stakes "War Room" feel
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    .panic-text { color: #ff4b4b; font-weight: bold; font-size: 24px; }
    .safe-text { color: #00ffcc; font-weight: bold; font-size: 24px; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOAD BRAIN
@st.cache_resource
def load_assets():
    model = joblib.load('panic_model.pkl')
    le = joblib.load('team_encoder.pkl')
    return model, le

model, team_le = load_assets()

# --- HEADER ---
st.title("🚨 IPL Tactical Command Center")
st.markdown("### *Phase: The Chasing Crisis (Over 10 Analysis)*")
st.divider()

# --- STEP 1: THE MISSION ---
st.header("Step 1: The Battlefield")
c1, c2, c3 = st.columns(3)

with c1:
    team = st.selectbox("Your Team (Chasing)", team_le.classes_)
    target = st.number_input("Target to Reach", 120, 260, 185)
with c2:
    curr_score = st.slider("Current Score (at Over 10.0)", 40, 150, 80)
    wickets = st.slider("Wickets Lost", 0, 9, 3)
with c3:
    season = st.number_input("IPL Season", 2008, 2026, 2024)

# --- INTERNAL CALCULATIONS ---
rrr = (target - curr_score) / 10
rrr_gradient = (rrr - (target/20)) / 10
res_score = 60 / (rrr + 1)
team_enc = team_le.transform([team])[0]

# --- STEP 2: THE PREDICTION ---
st.header("Step 2: The Stress Analysis")

# Animation for "Processing"
with st.spinner('Analyzing game momentum...'):
    time.sleep(0.5)

# Prep features for model
features = np.array([[target, curr_score, wickets, rrr, rrr_gradient, res_score, season, team_enc]])
panic_over = model.predict(features)[0]

# Visualizing the Stress
col_left, col_right = st.columns([1, 2])

with col_left:
    st.metric("Predicted Panic Over", f"Over {round(panic_over, 1)}")
    if panic_over <= 13:
        st.error("CRITICAL: Team will panic within the next 3 overs!")
    elif panic_over <= 16:
        st.warning("HIGH PRESSURE: Mid-innings collapse likely.")
    else:
        st.success("STABLE: The chase is under control.")

with col_right:
    # Custom Stress Meter using a progress bar
    stress_level = max(0, min(100, (20 - panic_over) * 10)) # Inverting over to get stress
    st.write("### Match Stress Meter")
    st.progress(int(stress_level))
    st.caption("0% = Calm | 100% = Immediate Collapse")

# --- STEP 3: THE GAME-CHANGER (SWAP PLAYER) ---
st.divider()
st.header("Step 3: Tactical Timeout 🛠️")
st.write("You have one chance to swap your current batsman for a **'Clutch Finisher'**. How does it change the future?")

if st.button("EXECUTE PLAYER SWAP"):
    # Simulated Impact: A finisher manages the RRR better, keeping the score 12 runs higher
    sim_score = curr_score + 12 
    sim_rrr = (target - sim_score) / 10
    sim_grad = (sim_rrr - (target/20)) / 10
    
    sim_features = np.array([[target, sim_score, wickets, sim_rrr, sim_grad, res_score, season, team_enc]])
    new_panic = model.predict(sim_features)[0]
    delay = new_panic - panic_over
    
    st.balloons()
    st.subheader("Result of the Tactical Swap:")
    st.markdown(f"By bringing in a high-impact player, you have delayed the panic window by **{round(delay, 1)} overs**.")
    st.markdown(f"The new predicted Panic Over is **{round(new_panic, 1)}**.")
    
    if delay > 1:
        st.write("✅ **Tactical Success:** You have given your team breathing room to finish the game.")
    else:
        st.write("⚠️ **Warning:** Even with the swap, the target is too high. The pressure remains critical.")

# --- FOOTER ---
st.sidebar.markdown("""
### How to Play:
1. **Set the Scene:** Input the match target and current score.
2. **Watch the Meter:** See how close the team is to "Panicking" (forced high-risk shots).
3. **Save the Game:** Use the 'Tactical Swap' to see how much of a difference a better player makes.
""")
