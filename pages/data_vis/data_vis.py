"""
A page of the application.
Page content is imported from the data_vis.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""
import pandas as pd
from taipy.gui import Markdown
from algorithms.model import get_team_goal_probability_distribution

data = pd.read_csv('data/stats.csv', usecols=['Team','Avg'])
team_list = list(data.Team.values)
team_selected = 'Argentina'
avg_goals = data[data.Team == team_selected].Avg.values[0]
goal_probability = get_team_goal_probability_distribution(avg_goals)

layout = {
  "xaxis": {
    # Force the title of the x axis
    "title": "# of goals"
  },
  "yaxis": {
    # Force the title of the x axis
    "title": "probability"
  },
}

def on_team_change(state):
    state.team_selected = data[data.Team == state.team_selected].Team.values[0]
    #state.team_selected = 'France'
    state.avg_goals = data[data.Team == state.team_selected].Avg.values[0]
    state.goal_probability = get_team_goal_probability_distribution(state.avg_goals, match_duration_in_seconds=90*60)

data_vis = Markdown("pages/data_vis/data_vis.md")

