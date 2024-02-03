import numpy as np

def get_match_probabilities(segment_length=30, segments_bought=6, match_duration=90*60):
    '''
    Calculate the probabilities of ad given that a goal happened P(ad ∩ goal) given the
    match, ad and goal duration
    '''
    goal_duration = 1  # Duration of the goal event
    ads_duration = segment_length  # Duration of the publicity (the ad is shown behind the goalkeeper this amount of time in each segment)
    ads_per_match = segments_bought   # Number of ads segments per match. Total ad time buyed by the client is ads_duration * ads_per_match
    
    max_goal_number = 10  # more than 10 goals per match is very unlikely for most of the teams
    seconds_per_match = match_duration # 90*60 = two times of 45 minutes

    number_of_simulations = 2200

    # The probability of P(ad ∩ goal) calculated by montecarlo simulation
    ad_and_goal_probability = [0]
    for ngoals in range(1,max_goal_number+1):
        events = 0
        _match = np.zeros(seconds_per_match, dtype=int)
        for sim in range(number_of_simulations):
            # Randomly choose the time of the start of a goal
            goal_indices = np.random.choice(seconds_per_match - goal_duration, ngoals, replace=False)
            goal_seconds = np.zeros(seconds_per_match, dtype=int)
            for idx in goal_indices:
                goal_seconds[idx:idx+goal_duration] = 1
            # Randomly choose the time of the start of the adds
            ad_seconds = np.zeros(seconds_per_match, dtype=int)
            # avoid ad overlaping
            segments = [st for st in range(1,match_duration+1, match_duration//ads_per_match)]+[match_duration]
            segments = list(zip(segments, segments[1:]))
            ad_indices  = [np.random.randint(s1,s2-ads_duration) for s1,s2 in segments]
            for idx in ad_indices:
                ad_seconds[idx:idx+ads_duration] = 1
            events += sum(goal_seconds & ad_seconds)  # the number of seconds in which there is a goal and the ad is behind the goalkeeper.
        prob = events/number_of_simulations
        ad_and_goal_probability.append(prob)
        #print(f'Goals: {ngoals}: probability: {prob}')
    return ad_and_goal_probability

def get_team_goal_probability_distribution(average_goals_per_match, match_duration_in_seconds=90*60):
    '''
    Calculate the goal probabilities as  X ~ Binom(average_goals_per_match, average_goals_per_match/match_duration_in_seconds)
    The function returns the array of probabilities of 0 goals, 1 goal, 2 goals,...
    given the average number of goals per match for a given team
    '''
    n_experiments = 10**6
    p = np.random.binomial(match_duration_in_seconds, average_goals_per_match/match_duration_in_seconds, n_experiments)
    probabilities = []
    for goals in sorted(list(set(p))):
        probabilities.append(sum(p == goals)/n_experiments)
    return probabilities

def get_conditional_probability(p_intersection, p_goal):
    return np.sum([p*q for p,q in zip(p_intersection,p_goal)])
