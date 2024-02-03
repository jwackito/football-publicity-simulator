"""
A page of the application.
Page content is imported from the prediction.md file.

Please refer to https://docs.taipy.io/en/latest/manuals/gui/pages for more details.
"""

import pandas as pd
import numpy as np
from taipy.gui import Markdown
from algorithms.model import get_team_goal_probability_distribution, get_match_probabilities

data = pd.read_csv('data/stats.csv', usecols=['Team','Avg'])
team_list = list(data.Team.values)
team_selected = 'Argentina'
avg_goals = data[data.Team == team_selected].Avg.values[0]
goal_probability = get_team_goal_probability_distribution(avg_goals)

# Configurable
ad_duration = 30
ad_segments = 6
match_duration = 90*60

# results
goal_and_ad_probability = get_match_probabilities(segment_length=ad_duration, segments_bought=ad_segments, match_duration=90*60)
probability = np.sum([p*q for p, q in zip(goal_probability, goal_and_ad_probability)])
prob_percent = probability*100

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
    state.probability = np.sum([p*q for p, q in zip(state.goal_probability, state.goal_and_ad_probability)])
    state.prob_percent = state.probability*100

def run_montecarlo(state):
    state.goal_and_ad_probability = get_match_probabilities(segment_length=state.ad_duration, segments_bought=state.ad_segments, match_duration=90*60)
    state.probability = np.sum([p*q for p, q in zip(state.goal_probability, state.goal_and_ad_probability)])
    state.prob_percent = state.probability*100

prediction = Markdown("pages/prediction/prediction.md")
