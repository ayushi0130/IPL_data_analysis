## IPL Data Analysis

This project involves an analysis of IPL data from 2008 to 2020. The data is analyzed to explore various aspects of the game, such as team performance, player performance, and trends over the years.

### Libraries Used

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, plot, iplot
```

### Datasets

The analysis uses two main datasets:

1. IPL Ball-by-Ball Data (IPL_Ball_by_Ball_2008_2020.csv): Contains detailed information about each ball bowled in the IPL matches.
2. IPL Match Data (IPL_Matches_2008_2020.csv): Contains match-level data, including details about the teams, players, and outcomes.

### Python Script Overview

The Python script (ipl_data_analysis.py) performs the following tasks:

#### Loading the Data:

Loads the ball-by-ball and match data into Pandas DataFrames.

#### Basic Data Exploration:

- Displays the first few rows of the data and basic statistics.

- Provides insights into unique values for venues, cities, teams, and players.

#### Batsman Performance Analysis:

Focuses on specific players, such as MS Dhoni, analyzing their performance based on runs, dismissals, and other metrics.

#### Toss Decisions Analysis:

Analyzes the decisions made by teams upon winning the toss, across different seasons.

#### Correlation Between Toss and Match Winning:

Investigates whether winning the toss correlates with winning the match.

#### Tournament Winners:

Identifies the teams that have won the IPL tournament the most.

#### Comparative Analysis of Teams:

Provides a comparative analysis of different teams based on matches played and wins.

### Visualizations

The script uses various visualization libraries, including:

1. Matplotlib: For creating basic plots.
2. Seaborn: For statistical visualizations.
3. Plotly: For interactive plots.

Running the Script

1. Clone this repository:

```
git clone https://github.com/ayushi0130/ipl-data-analysis.git
cd ipl-data-analysis
```

2. Place the datasets (IPL_Ball_by_Ball_2008_2020.csv and IPL_Matches_2008_2020.csv) in the repository directory.

Run the Python script:

```
python ipl_data_analysis.py
```

Result:

1.  Batsman performance analysis:

2.  Toss decision analysis:

3.  Does winning toss implies winning match:

4.  which team have won the tournment most:

        'Mumbai Indians': 5

5.  comparitive analysis of teams:
