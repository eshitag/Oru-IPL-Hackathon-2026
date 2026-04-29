# IPL: The Hidden Economy of Pressure 🏏📊 

## Executive Summary

In professional T20 cricket, traditional metrics like "Season Averages" often hide the most critical truth: Not all runs are created equal. This project introduces a "Pressure Engine" that quantifies the psychological and statistical "tax" applied to players when the Required Run Rate (RRR) spikes.

By merging ball-by-ball IPL data (2008–2025) with real-time match outcomes, I identified the "Ice-Kings"—players who defy the league-wide 47% increase in wicket probability to deliver outsized returns when the game is on the line.


![getsitecontrol__convert-video-to-gif__free](https://github.com/user-attachments/assets/5f595bf4-b7b4-4745-ac44-b5c1ee9dca69)

Project Panic is an end-to-end analytics platform that identifies the "Ice-Kings" of the IPL. Moving beyond static charts, this project features a Machine Learning-powered Tactical Command Center that predicts the exact over a team will collapse and simulates how deploying specific "Clutch" finishers can stay the "Panic Button" and flip the win probability.

## 🛠️ The Tech Stack
Data Processing: Python (Pandas, NumPy)

Analysis: Jupyter Notebook (Dimensional Modeling, ETL)

Visualization: Tableau (Dynamic Parameters, Dual-Axis Donut Charts, Highlight Actions)

Machine Learning: Scikit-Learn (Random Forest Regressor), Joblib for Model Serialization.

Interactive UI: Streamlit (Custom CSS, Session State Management).

Advanced Viz: Plotly (Radar Charts, Interactive Probability Timelines), Tableau.

Data Source: 300,000+ rows of IPL ball-by-ball delivery data.

## 🧠 The Narrative Flow (End-to-End)
1. Defining the "Pressure Zone"
The project started in Jupyter Notebook, where I moved beyond basic stats to engineer a dynamic environment.

The RRR Engine: Calculated the Required Run Rate for every delivery in the second innings.

The Pressure Flag: Developed a parameter-driven logic to segment play into "Normal" vs. "High Pressure" states.

Metric Engineering: Created custom calculations for Wicket Probability (Risk) and Clutch Strike Rate (Efficiency).

2. The Dashboard Story
The Tableau dashboard is designed as a "Scouting Tool" for franchises:

Pressure Exposure: My analysis reveals that only ~8% of the match (at a threshold of 14 RRR) constitutes high-pressure play. This proves that a tiny fraction of the game determines the champion.

Wicket Probability: As shown in the dynamic KPI block, once the "Panic Button" is pressed, the Wicket Probability jumps to 8.91%—nearly double the league average baseline.

The Level-Up Scatter Box: This is the heart of the analysis.

  X-Axis: Normal Strike Rate (The baseline).
  Y-Axis: Clutch Strike Rate (The performance under fire).
  "Players shown as outliers are statistical anomalies who score faster when the stakes are higher."

The Clutch-Impact Gap: A specialized leaderboard ranking the "Ice-Kings." The dashboard highlights players like Odean Smith and Glenn Phillips, who show massive performance gains in the death overs.

## 📈 Key Insights & Findings
The "Wicket Tax": Across all seasons, entering the Pressure Zone (RRR > 10) imposes a 40-50% increase in risk (Wicket Prob), yet the average league efficiency (Strike Rate) often remains stagnant.

The Survival Gap: Only 27.50% of teams facing the selected 14 RRR threshold go on to win the match, highlighting the extreme difficulty of the "Hidden Economy."

The Ice-King Anomaly: A very small subset of "underrated" players consistently outperform superstars when the RRR exceeds 12, providing high-value scouting targets for auctions.

## 🚀 How to Use the Dashboard
Set the Panic Button: Use the Pressure Threshold Slider (8 to 18) to define what you consider "Pressure." Watch as the KPIs and Scatter Plot recalibrate instantly.

Filter by Season: Analyze how a player's composure has evolved over the last 18 years.

Identify the Gems: Look at the top-right quadrant of the Scatter Box to find players who "Level Up."

## 📂 Repository Structure
notebooks/: ETL, Descriptive Analysis, and Model Training (PredictiveAnalysis.ipynb).

models/: Serialized .pkl files for the Random Forest model and Team Encoders.

app.py: The Streamlit Tactical Command Center source code.

data/: clutch_players.csv — The curated roster of high-impact specialists.

# ML Implementation: The AI Tactical Command Center 🏏📊

<img width="1152" height="648" alt="download" src="https://github.com/user-attachments/assets/2ba427a8-8743-4cd9-ae56-be109cdc5579" />


## The Predictive Brain (Machine Learning)

I trained a Random Forest model to predict the "Panic Over"—the specific point in an innings where the combination of wickets lost, RRR, and historical era trends makes a collapse statistically inevitable.

Feature Importance: The model identified that RRR Gradient and Wickets Lost are the primary drivers of the "Panic Button."

Era Calibration: The model accounts for "Era-Specific" scoring, recognizing that a 12 RRR in 2010 carries more psychological weight than in the high-scoring 2024 season.

## The Tactical Command Center (Streamlit)

The final output is a high-stakes simulation app structured in three acts:

Act 1: The Briefing: Users set the mission parameters (Target, Team, and Era).

Act 2: The Crisis: Users input the current match status at the 10-over mark.

Act 3: The Intervention: A "Character Select" system where users deploy a Lead Finisher. The AI then re-calculates the trajectory, showing a real-time shift in the Panic Over and Win Probability.

💬 Conclusion
This project moves data analytics from descriptive (what happened) to diagnostic (why it happened). It provides a framework for franchises to stop buying "runs" and start buying "resilience."

The Wicket Tax: Entering the Pressure Zone (RRR > 10) imposes a 47% increase in wicket probability league-wide.

The Panic Threshold: Most mid-tier teams hit their "Panic Button" by Over 14.5 when chasing 10+ RRR.

The Hero Effect: Deploying a top-tier "Ice-King" (players with a positive Clutch-Impact Gap) can delay the predicted collapse by an average of 1.8 to 2.5 overs.

## 🚀 How to Run the Simulator

Clone the Repo: git clone ...

Install Dependencies: pip install -r requirements.txt

Run the App: streamlit run app.py

Simulate: Choose your era, set a target, and select a "Hero" to see if you can beat the AI's predicted collapse.
_______________________________________________________________________________

Author: Eshita Gupta

Role: Business Intelligence & Data Engineering Professional

Location: St. John's, NL, Canada
