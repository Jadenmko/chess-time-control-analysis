# Chess Time Control vs. Rating Gap Analysis

Analysis of how time control affects the relationship between rating gap and win percentage in online chess, using pandas and matplotlib.

## Research Question
Does time control widen or narrow the effect of rating gap on win percentage?

## Key Finding
Rating gap predicts win% almost identically in Blitz and Rapid, but the effect is measurably weaker in Classical.

## Results
- Blitz (n=3,939): 28.10 percentage point spread (win% at High rating gap vs. Negligible)
- Rapid (n=14,385): 28.15 percentage point spread
- Classical (n=1,603): 20.87 percentage point spread (~7.3pp lower than Blitz/Rapid)

## Methodology
- Dataset: online chess games (`games.csv`)
- Tools: pandas, matplotlib
- Time control categorized by base minutes: Bullet <3, Blitz 3-10, Rapid 10-25, Classical 25+
- Rating gap categorized: Negligible 0-50, Low 50-100, Medium 100-200, High 200+
- Draws counted as 0.5 win for each side
- 203 games with tied ratings default to "black" as the higher-rated side; judged non-biasing given overall sample size, not corrected
- Bullet excluded from analysis: only 131 games total, unreliable sample size
- Dataset source: [Chess Game Dataset (Lichess)](https://www.kaggle.com/datasets/datasnaek/chess) — Kaggle

## How to Run
```
pip install pandas numpy matplotlib
python Chess_Time_Control_Analysis.py
```
Requires `games.csv` in the same directory.
## Charts

![Win Percentage by Skill Gap](chart1_win_pct.png)

![Sample Size per Bin](chart2_sample_size.png)

## Full Writeup
See [writeup.md](writeup.md) for the complete analysis and recommendation.

## Author
Jaden Ko — [GitHub](https://github.com/Jadenmko)
