# IPL: The Hidden Economy of Pressure 🏏📊

## Executive Summary

In professional T20 cricket, traditional metrics like "Season Averages" often hide the most critical truth: Not all runs are created equal. This project introduces a "Pressure Engine" that quantifies the psychological and statistical "tax" applied to players when the Required Run Rate (RRR) spikes.

By merging ball-by-ball IPL data (2008–2025) with real-time match outcomes, I identified the "Ice-Kings"—players who defy the league-wide 47% increase in wicket probability to deliver outsized returns when the game is on the line.

🛠️ The Tech Stack
Data Processing: Python (Pandas, NumPy)

Analysis: Jupyter Notebook (Dimensional Modeling, ETL)

Visualization: Tableau (Dynamic Parameters, Dual-Axis Donut Charts, Highlight Actions)

Data Source: 300,000+ rows of IPL ball-by-ball delivery data.

🧠 The Narrative Flow (End-to-End)
1. The Engineering: Defining the "Pressure Zone"
The project started in Jupyter Notebook, where I moved beyond basic stats to engineer a dynamic environment.

The RRR Engine: Calculated the Required Run Rate for every delivery in the second innings.

The Pressure Flag: Developed a parameter-driven logic to segment play into "Normal" vs. "High Pressure" states.

Metric Engineering: Created custom calculations for Wicket Probability (Risk) and Clutch Strike Rate (Efficiency).

2. The Dashboard Story: A 4-Stage Breakdown
The Tableau dashboard (see screenshot) is designed as a "Scouting Tool" for franchises:

The Hook (Pressure Exposure): My analysis reveals that only ~8% of the match (at a threshold of 14 RRR) constitutes high-pressure play. This proves that a tiny fraction of the game determines the champion.

The Physics (Wicket Probability): As shown in the dynamic KPI block, once the "Panic Button" is pressed, the Wicket Probability jumps to 8.91%—nearly double the league average baseline.

The Level-Up Scatter Box: This is the heart of the analysis.

X-Axis: Normal Strike Rate (The baseline).

Y-Axis: Clutch Strike Rate (The performance under fire).

The Diagonal Line: Represents the "Survival Line." Players above the line are statistical anomalies who score faster when the stakes are higher.

The Clutch-Impact Gap: A specialized leaderboard ranking the "Ice-Kings." The dashboard highlights players like Odean Smith and Glenn Phillips, who show massive performance gains in the death overs.

📈 Key Insights & Findings
The "Wicket Tax": Across all seasons, entering the Pressure Zone (RRR > 10) imposes a 40-50% increase in risk (Wicket Prob), yet the average league efficiency (Strike Rate) often remains stagnant.

The Survival Gap: Only 27.50% of teams facing the selected 14 RRR threshold go on to win the match, highlighting the extreme difficulty of the "Hidden Economy."

The Ice-King Anomaly: A very small subset of "underrated" players consistently outperform superstars when the RRR exceeds 12, providing high-value scouting targets for auctions.

🚀 How to Use the Dashboard
Set the Panic Button: Use the Pressure Threshold Slider (8 to 18) to define what you consider "Pressure." Watch as the KPIs and Scatter Plot recalibrate instantly.

Filter by Season: Analyze how a player's composure has evolved over the last 18 years.

Identify the Gems: Look at the top-right quadrant of the Scatter Box to find players who "Level Up."

📂 Repository Structure
notebooks/: Contains the .ipynb file for data cleaning, merging, and RRR calculation.

data/: Sample of the tableau_ready_ipl.csv (Fact & Dimension tables).

visuals/: Dashboard screenshots and Loom video link.

💬 Conclusion
This project moves data analytics from descriptive (what happened) to diagnostic (why it happened). It provides a framework for franchises to stop buying "runs" and start buying "resilience."

Author: Eshita Gupta

Role: Business Intelligence & Data Engineering Professional

Location: St. John's, NL, Canada
