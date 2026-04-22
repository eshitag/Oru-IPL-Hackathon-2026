import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the brain of the app
model = joblib.load('panic_model.pkl')
team_le = joblib.load('team_encoder.pkl')

st.set_page_config(page_title="IPL Panic Predictor", page_icon="🚨", layout="wide")

# Custom CSS for the "Finalist" Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏏 IPL Panic Over Predictor")
st.markdown("### Predicting the 'Hidden Economy' shift in real-time.")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("Match Context")
    season = st.number_input("Season", 2008, 2025, 2024)
    target = st.number_input("Target Score", 100, 260, 180)
    team = st.selectbox("Chasing Team", team_le.classes_)
    
    st.divider()
    st.header("Game State (at Over 10)")
    curr_score = st.slider("Current Score", 40, 140, 85)
    wickets = st.slider("Wickets Lost", 0, 9, 3)

# --- CALCULATIONS ---
# Calculate the features the model needs
rrr = (target - curr_score) / 10
rrr_gradient = (rrr - (target/20)) / 10
res_score = 60 / (rrr + 1)
team_enc = team_le.transform([team])[0]

# --- THE SIMULATOR ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Scenario A: Current Play")
    # Base features
    base_features = np.array([[target, curr_score, wickets, rrr, rrr_gradient, res_score, season, team_enc]])
    pred_a = model.predict(base_features)[0]
    st.metric("Panic Over", f"Over {round(pred_a, 1)}")

with col2:
    st.subheader("Scenario B: The 'Ice-King' Swap")
    # WHAT IF: You have a better finisher who keeps the score 10 runs higher?
    sim_score = curr_score + 15
    sim_rrr = (target - sim_score) / 10
    sim_grad = (sim_rrr - (target/20)) / 10
    
    sim_features = np.array([[target, sim_score, wickets, sim_rrr, sim_grad, res_score, season, team_enc]])
    pred_b = model.predict(sim_features)[0]
    
    st.metric("Panic Over", f"Over {round(pred_b, 1)}", delta=f"{round(pred_b - pred_a, 1)} overs delay")

st.info("💡 **Scenario B** simulates swapping in a high-impact finisher who maintains a higher run rate by Over 10, delaying the 'Panic Window'.")
