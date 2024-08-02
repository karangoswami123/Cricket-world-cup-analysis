import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from file_handling import load_data
from data_cleaning import clean_data

# Load and clean data
dataframes = load_data()
for year in dataframes:
    if dataframes[year] is not None:
        dataframes[year] = clean_data(dataframes[year])

# Sidebar for selecting the World Cup year
st.sidebar.title("Cricket World Cup Analysis")
year = st.sidebar.selectbox("Select World Cup Year", list(dataframes.keys()))

# Load the selected year's data
df = dataframes[year]

# Display data
st.title(f"Cricket World Cup {year} Analysis")
st.write("## Data Preview")
st.dataframe(df.head())

# Total Runs per Team
st.write("## Total Runs per Team")
total_runs = df.groupby('TEAM')['RUNS SCORED'].sum()
st.bar_chart(total_runs , color='#fffe')

# Pie Chart for Proportion of Total Runs
st.write("## Proportion of Total Runs by Team")
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(total_runs, labels=total_runs.index, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
for text in texts:
    text.set_fontsize(10)
for autotext in autotexts:
    autotext.set_fontsize(8)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.legend(wedges, total_runs.index, title="Teams", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
st.pyplot(fig)

# Total Wickets Taken per Team
st.write("## Total Wickets Taken per Team")
total_wickets = df.groupby('TEAM')['WICKETS TAKEN'].sum()
st.bar_chart(total_wickets)

# Determine Tournament Winner
tournament_winner = total_runs.idxmax()
st.write("## Tournament Winner")
st.write(f"The winner of the Cricket World Cup {year} is {tournament_winner}!")

# Summary
st.write("## Summary")
summary = []
summary.append(f"World Cup {year} Summary:")
summary.append("Total Runs Scored by Each Team:")
summary.extend([f"{team}: {runs}" for team, runs in total_runs.items()])
summary.append("\nTotal Wickets Taken by Each Team:")
summary.extend([f"{team}: {wickets}" for team, wickets in total_wickets.items()])

summary_text = "\n".join(summary)
st.text_area("Summary", summary_text)

# Save summary to file
summary_path = f"Cricket_World_Cup_Summary_{year}.txt"
with open(summary_path, "w") as file:
    file.write(summary_text)
st.write(f"Summary saved to {summary_path}")

# Detailed Textual Summary
st.write("## Detailed Summary")
top_scorer = total_runs.idxmax()
top_scorer_runs = total_runs.max()
top_bowler = total_wickets.idxmax()
top_bowler_wickets = total_wickets.max()

detailed_summary = (
    f"The {year} Cricket World Cup showcased incredible performances from all participating teams. "
    f"Analyzing the data, we observe that {top_scorer} emerged as the top-scoring team, amassing a total of {top_scorer_runs} runs. "
    f"This achievement underscores their formidable batting lineup, which outperformed other teams in terms of run accumulation. "
    f"On the bowling front, {top_bowler} led the pack by taking the most wickets, with a total of {top_bowler_wickets} wickets. "
    f"Their bowling prowess was instrumental in restricting opponents' scores and securing victories. "
    f"Overall, the tournament was a testament to the high level of competition and skill displayed by all teams, making it a memorable event in cricket history."
)
st.write(detailed_summary)

