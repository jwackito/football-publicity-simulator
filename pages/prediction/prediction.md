# Prediction

## 1. Cofigure Ad and Match Properties. 
<|layout|columns=1 1 1 1|
Ad Duration in seconds

<|{ad_duration}|slider|min=10|max=200|>

<p></p>

<p></p>	

Number of segments bought

<|{ad_segments}|slider|min=1|max=20|>

<p></p>	

<p></p>	

Match length

<|{match_duration}|slider|min=5400|max=6000|>

<p>Match length in seconds. A 90 minutes match will be 5400 seconds and a 90+10 minutes (two overtimes of 5 minutes) will be 6000.</p>	

<|Run Montecarlo|button|on_action=run_montecarlo|>
|>

## 2. Choose your team
<|layout|columns=1 1|

<|{team_selected}|selector|lov={team_list}|dropdown|on_change=on_team_change|>

### Goal Probability Distribution for <|{team_selected}|>

<|Team average goals {avg_goals}|>


<|{goal_probability}|chart|layout={layout}|>

<p></p>	

<p style="text-align: center;font-style: italic;"><i>Probability of the team of scoring exactly <b># of goals</b> in a given match.</i></p>

|>


<|card|
<center>
<|{prob_percent:0.2f}%|> (Uncertainties provided in the subscription version :P)
</center>
|>
