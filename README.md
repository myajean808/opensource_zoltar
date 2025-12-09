# `def opensource_zoltar:`
# **✧･ﾟ:✧* Cards are random, people are not. ･ﾟ:*✧･ﾟ:*✧･ﾟ:*

This project explores the intersection of intuition and probability by recreating tarot readings through computational simulation. I designed a dataset, virtual tarot reader, and simulation that mimics authentic shuffling techniques, card selection, and interpretive practices. I then repeated this simulation 10,000 times and verified the randomness of its readings. I incorporated Claude (a Large Language Model) as the "reader" to explore how machine interpretation compares to traditional human understanding. Feel free to make contributions.

Files in This Repository

1. `stat_tarot.ipynb` - Main Jupyter notebook containing analysis and visualizations

2. `tarot.csv` - Tarot card dataset with traditional meanings and associations

3. `tarot.py` - Core tarot card class and reading generation functions

4. `simulation_summary.csv` - Summary statistics from simulation runs

5. `simulation.py` - Simulation engine for generating multiple readings

6. `visualizations.py` - Plotting functions for data visualization

7. `tables.py` - Statistical tables and summary generation

# Usage
```python
# Example: Generate a single reading
from tarot import generate_reading
reading = generate_reading(spread_type="three_card")

# Example: Run simulation
from simulation import run_simulation
results = run_simulation(n_readings=10000)

# Example: Visualize results
from visualizations import plot_distribution
plot_distribution(results)
```

# Requirements

Python 3.8+
Jupyter Notebook environment (Anaconda, etc.)

Install dependencies:
```bash
# follow this structure if you're missing others
pip install pandas numpy matplotlib seaborn jupyter
```

# Theoretical Background
This project is inspired by work in:

* Cognitive psychology (pattern recognition, confirmation bias)
* Philosophy of probability (subjective vs. objective interpretations)
* Simulation Methods and Statistical Computing

# Contributing
Areas of interest:

* Additional statistical tests
* Alternative visualization approaches
* Theoretical framework development
* Cross-validation with human reading data

# License
MIT License.

# Citation
If you use this code or methodology in your research, please cite:
[Mya Strayer]. Open Source Zoltar. 
GitHub repository: https://github.com/myajean808/opensource_zoltar

## Contact
mya.j.strayer@gmail.com
