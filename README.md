# Chess Time Control vs. Rating Gap Analysis

Analysis of how time control affects the relationship between rating gap and win percentage in online 
chess, using pandas and matplotlib.

## Research Question
Does time control widen or narrow the effect of rating gap on win percentage?

## Key Finding
While time control has a negligible impact on the predictive power of rating gaps in Blitz and Rapid, 
it becomes a measurable factor in Classical games.

## Methodology
- Dataset: online chess games (games.csv)
- Tools: pandas, matplotlib
- Players categorized by rating gap (Negligible/Low/Medium/High) and game categorized by time control 
(Bullet/Blitz/Rapid/Classical)
- Bullet excluded from analysis due to insufficient sample size (131 games)

## Charts

![Win Percentage by Skill Gap](chart1_win_pct.png)

![Sample Size per Bin](chart2_sample_size.png)

## Full Writeup
See [writeup.txt](writeup.txt) for the complete analysis and recommendation.

