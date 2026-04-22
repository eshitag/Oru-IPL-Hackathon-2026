import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. LOAD ASSETS
@st.cache_resource
def load_game_data():
    model = joblib.load('panic_model.pkl')
    team_le = joblib.load('team_encoder.pkl')
    # Load the player stats you created in your other notebook!
    player_stats = pd.read_csv('clutch_players.csv').set_index('batsman')
    return model, team_le, player_stats

model, team_le, player_stats = load_game_data()

st.title("🏏 IPL Tactical Commander: Elite Edition")

# --- SIDEBAR: MISSION SETUP ---
with st.sidebar:
    st.header("📍 Match Context")
    # Future-proofed the year
    season = st.slider("Season (Era)", 2008, 2030, 2025)
    target = st.number_input("Target Score", 100, 280, 200)
    chasing_team = st.selectbox("Your Franchise", team_le.classes_)
    
    st.divider()
    st.header("👤 Character Select")
    # Let the user pick a 'Hero' player to save the game
    hero_player = st.selectbox("Select Your Finisher", player_stats.index)
    clutch_ability = player_stats.loc[hero_player, 'clutch_gap']
    
    st.info(f"**{hero_player}'s Stats:**\nStrike Rate increases by {round(clutch_ability, 1)}% under pressure.")

# --- MAIN INTERFACE ---
st.header("The Crisis: Over 10.0")
col1, col2 = st.columns(2)

with col1:
    curr_score = st.number_input("Current Score", 0, target, 90)
with col2:
    wickets = st.slider("Wickets Lost", 0, 9, 4)

# Calculations
rrr = (target - curr_score) / 10
rrr_gradient = (rrr - (target/20)) / 10
res_score = 60 / (rrr + 1)
team_enc = team_le.transform([chasing_team])[0]

# Initial Prediction
base_features = np.array([[target, curr_score, wickets, rrr, rrr_gradient, res_score, season, team_enc]])
panic_over = model.predict(base_features)[0]

# --- THE RESULTS ---
st.divider()
res_col1, res_col2 = st.columns(2)

with res_col1:
    st.subheader("Original Timeline")
    st.metric("Predicted Panic", f"Over {round(panic_over, 1)}")
    
with res_col2:
    st.subheader(f"The {hero_player} Effect")
    
    # Logic: The 'Hero' player improves the team's score by their clutch_gap percentage
    # (e.g., if they increase SR by 20, we assume 10-15 extra runs by Over 10)
    impact_boost = (clutch_ability / 10) # Scaling for realism
    sim_score = curr_score + impact_boost
    sim_rrr = (target - sim_score) / 10
    sim_grad = (sim_rrr - (target/20)) / 10
    
    sim_features = np.array([[target, sim_score, wickets, sim_rrr, sim_grad, res_score, season, team_enc]])
    hero_panic = model.predict(sim_features)[0]
    
    delay = hero_panic - panic_over
    st.metric("New Panic Over", f"Over {round(hero_panic, 1)}", delta=f"{round(delay, 1)} overs delayed")

# --- NARRATIVE SUMMARY ---
if delay > 0.5:
    st.success(f"🌟 **Tactical Masterclass!** By deploying **{hero_player}**, you've pushed the panic window back. Their ability to score under pressure keeps the Required Rate manageable.")
else:
    st.error(f"💀 **Critical Failure.** Even with **{hero_player}** in the middle, the current scoreboard pressure is too high. A collapse is imminent.")

st.markdown(f"""
### Why this happened:
The model analyzed the **{season}** season dynamics and determined that with **{wickets}** wickets down, 
your current Required Run Rate of **{round(rrr, 2)}** is the tipping point. 
""")
