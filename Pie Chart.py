import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")

goals_column = 'Goals'
year_column = 'Year'
league_column = 'League' 

df_2016 = df[df[year_column] == 2016]

total_goals_2016 = df_2016[goals_column].sum()

goals_by_league = df_2016.groupby(league_column)[goals_column].sum() / total_goals_2016 * 100

plt.figure(figsize=(12, 8))
plt.pie(goals_by_league, labels=goals_by_league.index, autopct='%1.1f%%', startangle=90, counterclock=False)

plt.legend(title='Giải Đấu', bbox_to_anchor=(1, 0.5), loc="lower left")
plt.title('Phân bổ ghi bàn theo giải đấu (2016)', fontsize=16, fontweight='bold')

plt.show()
