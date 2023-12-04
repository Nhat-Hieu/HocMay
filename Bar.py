import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Top-Football-Leagues-Scorers2016-2019.csv")

selected_columns = ['Player Names', 'Goals']

df_top_scorers = df[selected_columns]

total_goals_by_player = df_top_scorers.groupby('Player Names')['Goals'].sum()

top_10_scorers = total_goals_by_player.nlargest(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(top_10_scorers.index, top_10_scorers, color='#1f78b4')

plt.xlabel('Cầu Thủ')
plt.ylabel('Số Lần Ghi Bàn (Bàn)')
plt.title('Top 10 Cầu Thủ Ghi Bàn Nhiều Nhất (2016-2019)', fontsize=16, fontweight='bold')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)

legend = plt.legend(["Số lần ghi bàn"], title='Chú thích', title_fontsize='12', fontsize='12')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
