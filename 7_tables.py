import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from tarot import tarot_reading

simulation_summary = pd.read_csv('simulation_summary.csv')

def fig1_stats():
    # accompanying statistics for figure 1
    mean = simulation_summary['Average Numerology'].mean()
    std = simulation_summary['Average Numerology'].std()
    
    fig1_stats = {
        'Mean Numerology Value': [f'{mean:.4f}'],
        'Standard Deviation': [f'{std:.4f}']
    }
    fig1_table = pd.DataFrame(fig1_stats)
    print(fig1_table.to_string(index=False))
    return

def fig2_stats():
    small = simulation_summary.sample(n=77,
                    random_state=808).sort_values('Run')
    small['Index'] = range(len(small))

    large = simulation_summary.sample(n=777,
                        random_state=808).sort_values('Run')
    large['Index'] = range(len(large))
    
    # accompanying statistics for figure 2
    small_iqr = np.percentile(small['Average Numerology'], 75) - np.percentile(small['Average Numerology'], 25)
    small_range = small['Average Numerology'].max() - small['Average Numerology'].min()
    large_iqr = np.percentile(large['Average Numerology'], 75) - np.percentile(large['Average Numerology'], 25)
    large_range = large['Average Numerology'].max() - large['Average Numerology'].min()
    
    fig2_stats = {
        'Subset': ['Smaller', 'Larger'],
        'IQR': [f'{small_iqr:.4f}', f'{large_iqr:.4f}'],
        'Range': [f'{small_range:.4f}', f'{large_range:.4f}']
    }
    fig2_table = pd.DataFrame(fig2_stats)
    print(fig2_table.to_string(index=False))
    return

def fig3_stats():
    # accompanying statistics for figure 3
    simulation_avg_valence = simulation_summary['Positivity Score'].mean()
    reading = tarot_reading()
    cards_avg_valence = reading['Valence'].mean()
    
    fig3_stats = {
        'Simulation Avg': [f'{simulation_avg_valence:.4f}'],
        'Reading Avg': [f'{cards_avg_valence:.4f}']
    }
    fig3_table = pd.DataFrame(fig3_stats)
    print(fig3_table.to_string(index=False))
    return

def convergence_run_number(series, mean, threshold=0.01, window=100):
    for i in range(len(series) - window):
        subset = series.iloc[i:i+window]
        if all(abs(subset - mean) / abs(mean) < threshold):
            return i + 1  # return run number
    return len(series)  # return total runs if never converged

def fig4_stats():
    summary = pd.read_csv('simulation_summary.csv')
    
    # accompanying statistics for figure 4
    correct_score = simulation_summary['Correct Guess'].mean()
    adjusted_score= simulation_summary['Adjusted Guess'].mean()
    
    # need to compare all the means
    correct_expanded = simulation_summary['Correct Guess'].expanding().mean()
    adjusted_expanded = simulation_summary['Adjusted Guess'].expanding().mean()
    
    # apply the function
    correct_convergence_run = convergence_run_number(correct_expanded, correct_score)
    adjusted_convergence_run = convergence_run_number(adjusted_expanded, adjusted_score)
    
    # save the stats
    fig4_stats = {
        ' ': ['Correct Rate', 'Adjusted Rate'],
        'Average Accuracy': [f'{correct_score:.4f}', f'{adjusted_score:.4f}'],
        '# Runs to Convergence': [f'{correct_convergence_run}', f'{adjusted_convergence_run}']
    }
    fig4_table = pd.DataFrame(fig4_stats)
    print(fig4_table.to_string(index=False))

    # egregious misuse of the t-test
    t_stat, p_value = stats.ttest_ind(summary['Correct Guess'], summary['Adjusted Guess'], equal_var=False)

    print(f'Test Statistic: {t_stat:.3f},')
    print(f'  p-value: {p_value:.8f}')
    return

def fig5_stats(reading, reading_history, reading_index):

    # Add index column to this reading
    reading['Index'] = reading_index
    
    # Append to history
    reading_history = pd.concat([reading_history, reading], ignore_index=True)
    
    # Calculate aggregate mean numerology
    mean_numerology = reading_history['Numerology'].mean()

    return reading_history, mean_numerology