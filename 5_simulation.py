import numpy as np
import pandas as pd
from tarot import tarot_reading

def run_simulation(run_num):
    ''' 
    Uses the functions I created to simulate a
    virtual tarot reading 10,000 times.
    '''
    # runs my simulation
    reading = tarot_reading()

    # find most common element
    most_common = reading['Element'].value_counts().idxmax()

    # return aggregate statistics for analysis
    return {
        'Run': run_num,
        'Average Numerology': reading['Numerology'].mean(),
        'Error Level': reading['Numerology'].mean() / 5, # accounting for small n
        'Major Element': most_common,
        'Positivity Score': reading['Valence'].mean(),
        # used to evaluate Claude as the reader
        'Correct Guess': reading['Alignment'].mean(),
        'Adjusted Guess': reading['Noisy Alignment'].mean()
    }

# runs above function 10000 times
simulation_summary = pd.DataFrame([
    run_simulation(i + 1) for i in range(10000)
])

# used to save the file
#simulation_summary.to_csv('simulation_summary.csv', index=False)