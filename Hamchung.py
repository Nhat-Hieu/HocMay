import pandas as pd
import matplotlib.pyplot as plt

def plot_top_scorers(data_file):
    df = pd.read_csv(data_file)

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

def plot_goals_distribution(data_file, year=2016):
    df = pd.read_csv(data_file)

    goals_column = 'Goals'
    year_column = 'Year'
    league_column = 'League' 

    df_year = df[df[year_column] == year]

    total_goals_year = df_year[goals_column].sum()

    goals_by_league = df_year.groupby(league_column)[goals_column].sum() / total_goals_year * 100

    plt.figure(figsize=(12, 8))
    plt.pie(goals_by_league, labels=goals_by_league.index, autopct='%1.1f%%', startangle=90, counterclock=False)

    plt.legend(title='Giải Đấu', bbox_to_anchor=(1, 0.5), loc="lower left")
    plt.title(f'Phân bổ ghi bàn theo giải đấu ({year})', fontsize=16, fontweight='bold')

    plt.show()

plot_top_scorers("Top-Football-Leagues-Scorers2016-2019.csv")
plot_goals_distribution("Top-Football-Leagues-Scorers2016-2019.csv")
