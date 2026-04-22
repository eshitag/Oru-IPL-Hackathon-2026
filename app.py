import streamlit as st
import joblib
import pandas as pd
import numpy as np
import time

# 1. THEME & ASSETS
st.set_page_config(page_title="IPL Tactical Command", page_icon="🚨", layout="wide")

@st.cache_resource
def load_assets():
    model = joblib.load('panic_model.pkl')
    le = joblib.load('team_encoder.pkl')
    player_stats = pd.read_csv('clutch_players.csv').set_index('batsman')
    return model, le, player_stats

model, team_le, player_stats = load_assets()

# 2. THE STORYBOARD UI
st.title("🚨 IPL TACTICAL COMMAND: PROJECT PANIC")
st.markdown("---")

# --- ACT 1: THE BRIEFING ---
with st.container():
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.header("📂 Mission Briefing")
        st.info("Incoming Transmission: Final 10 Overs remaining. The target is set. The era is defined. Choose your battlefield.")
    
    with col_b:
        c1, c2, c3 = st.columns(3)
        with c1:
            season = st.select_slider("Select Era (Difficulty)", options=list(range(2008, 2031)), value=2025)
        with c2:
            target = st.number_input("Target Score", 120, 280, 190)
        with c3:
            team = st.selectbox("Chasing Franchise", team_le.classes_)

# --- ACT 2: THE CRISIS ---
st.markdown("### ⚡ The Crisis: Over 10.0")
col_c, col_d, col_e = st.columns(3)

with col_c:
    curr_score = st.slider("Current Score", 40, target-20, 85)
with col_d:
    wickets = st.select_slider("Wickets Down", options=list(range(0, 10)), value=4)
with col_e:
    hero = st.selectbox("Assign Lead Finisher (Hero)", player_stats.index)

# CALCULATIONS (The Engine)
rrr = (target - curr_score) / 10
rrr_gradient = (rrr - (target/20)) / 10
res_score = 60 / (rrr + 1)
team_enc = team_le.transform([team])[0]
clutch_ability = player_stats.loc[hero, 'clutch_gap']

# PREDICTIONS
base_f = np.array([[target, curr_score, wickets, rrr, rrr_gradient, res_score, season, team_enc]])
panic_over = model.predict(base_f)[0]

# --- ACT 3: THE SIMULATION ---
st.markdown("---")
if st.button("🚀 INITIATE SIMULATION", use_container_width=True):
    with st.status("Calculating Trajectories...", expanded=True) as status:
        st.write(f"Analyzing {team}'s historical data for {season}...")
        time.sleep(1)
        st.write(f"Calculating {hero}'s impact on Required Run Rate...")
        time.sleep(1)
        status.update(label="Simulation Complete!", state="complete", expanded=False)

    # IMPACT LOGIC
    # We simulate that the Hero's 'Clutch Gap' delays the panic by improving the RRR efficiency
    impact_boost = (clutch_ability / 8) # Scaled impact
    sim_score = curr_score + impact_boost
    sim_rrr = (target - sim_score) / 10
    sim_grad = (sim_rrr - (target/20)) / 10
    
    sim_f = np.array([[target, sim_score, wickets, sim_rrr, sim_grad, res_score, season, team_enc]])
    hero_panic = model.predict(sim_f)[0]
    delay = hero_panic - panic_over

    # THE RESULTS (The Storyteller)
    res_1, res_2 = st.columns(2)
    
    with res_1:
        st.subheader("📊 Tactical Analysis")
        st.write(f"**Baseline Panic:** Over {round(panic_over, 1)}")
        stress = max(0, min(100, (18 - panic_over) * 15))
        st.write(f"Current Match Stress:")
        st.progress(int(stress))

    with res_2:
        st.subheader(f"🛡️ The {hero} Intervention")
        if delay > 0.5:
            st.metric("New Panic Window", f"Over {round(hero_panic, 1)}", delta=f"{round(delay, 1)} Overs Gained", delta_color="normal")
            st.success(f"**Coach's Report:** {hero} has successfully 'iced' the chase. By absorbing the {round(rrr,1)} RRR, they have pushed the panic threshold deeper into the death overs.")
            st.balloons()
        else:
            st.metric("New Panic Window", f"Over {round(hero_panic, 1)}", delta=f"{round(delay, 1)} Overs (Insufficient)", delta_color="inverse")
            st.error(f"**Coach's Report:** Even with {hero}, the math is failing us. The pressure gradient is too steep. We are predicted to collapse by Over {round(hero_panic, 1)}.")

# FOOTER
st.sidebar.markdown(f"""
### 📜 Mission Intel
- **The Target:** {target}
- **Required Rate:** {round(rrr, 2)}
- **Agent {hero}'s Record:** SR increases by {round(clutch_ability, 1)}% in the Pressure Zone.
""")
