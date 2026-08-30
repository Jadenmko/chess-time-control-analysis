import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
games = pd.read_csv('games.csv', index_col=0)

BULLET_MAX = 3
BLITZ_MAX = 10
RAPID_MAX = 25

games[["Time Control", "Increment"]] = games["increment_code"].str.split("+", expand= True)
games[["Time Control", "Increment"]] = games[["Time Control", "Increment"]].astype(int)

games["Category"] = pd.cut(games["Time Control"], bins= [0, BULLET_MAX, BLITZ_MAX, RAPID_MAX, np.inf], right=False, labels= ["Bullet", "Blitz", "Rapid", "Classical"])

"""Rating difference and win percentage mechanism"""
# 203 rating-tie games default to "black" via np.where — judged negligible/non-biasing given sample size, not corrected
games["Higher Rating"] = np.where(games["white_rating"] > games["black_rating"], "white", "black")

conditions = [
    games["winner"] == "draw",
    games["winner"] == games["Higher Rating"]
]
values = [0.5, 1]
games["Win Values"] = np.select(conditions, values, default=0)

games["Rating Diff"] = (games["white_rating"] - games["black_rating"]).abs()

games["Skill Gap"] = pd.cut(games["Rating Diff"], bins= [0, 50, 100, 200, np.inf], right=False, labels= ["Negligible", "Low", "Medium", "High"])

data = games.groupby(["Skill Gap", "Category"])["Win Values"].agg("mean") * 100
data = data.reset_index()
wide_data = data.pivot(index= "Skill Gap", columns= "Category", values= "Win Values")
wide_data = wide_data.drop(columns = "Bullet") # Bullet excluded: only ~131 games total, unreliable sample size (see Chart 2)
print(wide_data)

"""Visualization : Line + Bar Charts"""
fig, ax = plt.subplots() 

for category in wide_data: 
    ax.plot(wide_data.index, wide_data[category], marker= "o", label = category) 

ax.set_xlabel("Skill Gap")
ax.set_ylabel("Win Percentage")
ax.set_title("Win % by Skill Gap Across Time Controls")

ax.set_xticks([0,1,2,3]) 
ax.set_xticklabels(["Negligible\n(0-50)", "Low\n(50-100)", "Medium\n(100-200)", "High\n(200+)"]) 
ax.legend() 
plt.show()

bar_data = games.groupby(["Skill Gap", "Category"]).size().unstack()
print(bar_data)

x = np.arange(len(bar_data.index))   
width = 0.2                           
categories = bar_data.columns         

fig, ax = plt.subplots()

for i, category in enumerate(categories):
    offset = width * i
    ax.bar(x + offset, bar_data[category], width, label=category)

ax.set_xlabel("Skill Gap")
ax.set_ylabel("Number of Games")
ax.set_title("Sample Size per Skill Gap Bin by Time Control")
ax.set_xticks(x + width * 2)   
ax.set_xticklabels(bar_data.index)
ax.legend()
plt.show()
