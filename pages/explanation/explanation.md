# Publicity probability simulator

Do you ever wonder what is the probability of your ad being displayed in the precise moment of your favorite team scoring a goal?
<center>
<|images/messi.png|image|width=600px|>
</center>

This probability depends on many factors, including
<ul>
<li> the amount of time bought to the publicity agent </li>
<li> the probability of your team scoring a goal during a match </li>
<li> the length of the match </li>
</ul>

Using montecarlo simulations, it is possible to calculate two independent probabilities, the probability <b>P(goal)</b> of your team scoring a goal during a given match, and the probability <b>P(ad ∩ goal)</b> of your team scoring a goal while the ad of your brand is being displayed behind the goalkeep.
<p>
The probability <b>P(goal)</b> is based on the historical average amount of goals of your team. It can be modeled using a Binomial distribution. The probability <b>P(goal<sub>i</sub>)</b> of your team scoring exactly <b>i</b> goals is a random variable with distribution <b>X ~ Bin(n, p)</b> with <b>n</b> being the number of seconds played in a match and <b>p</b> the historical average of goals per match divided by the number of seconds played in the match. For Argentina, with an average number of goals per match of <b>2</b> and a normal football match of 90 minutes, the goal distribution is X ~ Bin(90*60, 2/(90*60)). You can see the distrubutions for several national teams in the DATA_VIS tab. The bigger the average the bigger the probability of scoring several goals. However, notice how unlikely is for ever team to score more than 10 goals.
</p><p>
The probability <b>P(ad ∩ goal)</b> can be calculated using montecarlo simulations for each amount of goals in a match. Obviously, if your team scores 0 goals, the probability <b>P(ad ∩ goal)</b> will be 0 too. But the more goals your team score in a match, the more probable <b>P(ad ∩ goal)</b> becomes. I calculated this probabilities independently for several different amount of goals (that is <b>P(ad ∩ goal<sub>i</sub>)</b>), but this distribution do not depend on the team scoring the goals. The simulator "plays" several matches, choosing at random the moment of a goal and the moment of and ad happening. After several simulations, is possible to compute the probability simply by counting the times the ad and the goal happen at the same time and dividing by the number of simulations.
</p><p>
As the two probabilities, <b>P(goal<sub>i</sub>)</b> and <b>P(ad ∩ goal<sub>i</sub>)</b> are independent, the final probability <b>P(ad ∩ goal|goal)</b> can be calculated as the sum of the product of the probabilities.
</p>
<center>
<|images/probcond.png|image|>
</center>
<p>
<center>
 --
</center>
</p>
