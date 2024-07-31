import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

deliveries_data = pd.read_csv('IPL_Ball_by_Ball_2008_2020.csv')
match_data = pd.read_csv('IPL_Matches_2008_2020.csv')

# Basic Analysis

print(match_data.head())
print(match_data.columns)
print(match_data.shape)
no_of_matches = match_data.shape[0]
print(no_of_matches)
print(match_data['venue'].unique())
print(match_data['city'].unique())

print(match_data['team1'].unique())

print(match_data['toss_winner'].value_counts().index[0])
print(match_data['player_of_match'].value_counts().index[0])

# In-Depth analysis of batsman performance

print(deliveries_data['batsman'].unique())

filt = deliveries_data['batsman']== 'MS Dhoni'

df_dhoni = deliveries_data[filt]

print(df_dhoni.columns)

print(df_dhoni['dismissal_kind'].value_counts())

print(df_dhoni['batsman_runs'].unique())

print(len(df_dhoni[df_dhoni['batsman_runs']==1]))

print(len(df_dhoni[df_dhoni['batsman_runs']==2])*2)

print(len(df_dhoni[df_dhoni['batsman_runs']==3])*3)

print(len(df_dhoni[df_dhoni['batsman_runs']==4])*4)

print(len(df_dhoni[df_dhoni['batsman_runs']==6])*6)

import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot

values = [1409, 630, 45, 1252, 1296]
labels = [1, 2, 3, 4, 6]

trace = go.Pie(labels=labels, values=values, hole=0.3)

data = [trace]

fig = go.Figure(data = data)

fig.show()

#Toss Decision across season

print(match_data.columns)

print(match_data['date'])

match_data['season'] = pd.to_datetime(match_data['date']).dt.year

season_toss_count_df = match_data.groupby(['season', 'toss_decision']).size().reset_index().rename(columns={0:'count'})

print(season_toss_count_df)

plt.figure(figsize=(10,8))
sns.barplot(x='season', y='count',hue='toss_decision',data=season_toss_count_df)
plt.show()

# Does winning toss implies winning game?

print(match_data[['team1','team2','toss_winner','winner']])

match_data['toss_win_game_win'] = np.where(match_data['toss_winner']==match_data['winner'],'Yes','No')

print(match_data['toss_win_game_win'].value_counts())

print(match_data['toss_win_game_win'].value_counts().index)
print(match_data['toss_win_game_win'].value_counts().values)

labels = match_data['toss_win_game_win'].value_counts().index
values = match_data['toss_win_game_win'].value_counts().values

trace = go.Pie(labels=labels, values=values, hole=0.3)

data = [trace]

fig = go.Figure(data = data)
fig.update_traces(hoverinfo= 'label+percent', textinfo = 'label+percent')
fig.show()

# which team have won the tournment most

print(match_data['season'].unique())

df_2018 = match_data[match_data['season']== 2018]

print(df_2018['winner'].tail().values[0])

winners_team ={}

for year in sorted(match_data['season'].unique()):
    current_yr_df = match_data[match_data['season']==year]
    winners_team[year]=current_yr_df['winner'].tail().values[0]

print(winners_team)
print(winners_team.values())

from collections import Counter
print(Counter(winners_team.values()))

# comparitive analysis of teams

print(match_data[['team1','team2']])
matches_played=match_data['team1'].value_counts() + match_data['team1'].value_counts()
matches_played_df = matches_played.to_frame().reset_index()
matches_played_df.columns = ['team_name', 'matches_played']
print(matches_played_df)
wins=pd.DataFrame(match_data['winner'].value_counts()).reset_index()
wins.columns = ['team_name','wins']
print(wins)

played = pd.merge(matches_played_df,wins,how='inner',on='team_name')

trace1 = go.Bar( 
    x = played['team_name'],
    y = played['matches_played'],
    name = 'total matches'
)

trace2 = go.Bar( 
    x = played['team_name'],
    y = played['wins'],
    name = 'total matches'
)

data = [trace1,trace2]

iplot(data)