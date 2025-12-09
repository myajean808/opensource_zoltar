# necessary imports
import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from matplotlib.collections import LineCollection

# add in my functions
from tarot import tarot_reading

# set the font for all visualizations
plt.rcParams['font.family'] = 'monospace'

simulation_summary = pd.read_csv('simulation_summary.csv')
cards = pd.read_csv('tarot.csv')

def figure_one():
    # initialize the figure with just one subplot
    figure1, ax = plt.subplots(1, 1, figsize=(10, 5))
    
    # set background color
    ax.set_facecolor('#f5f0e8')
    
    # only want to show grid behind the data
    ax.set_axisbelow(True)
    ax.grid(True, color='#c9c9c9')
    
    # bindwidth matters!
    ax = sns.histplot(simulation_summary, x='Average Numerology', binwidth=1, kde=True, color='#E67E50')

    # changing kde line color
    ax.lines[0].set_color('#C1440E')
    
    # plot display settings
    ax.set_xlabel('Average Numerology Value', fontsize=12)
    ax.set_ylabel('Count', fontsize=14)
    
    # overall figure display settings (title only, no subtitle)
    figure1.suptitle('Numerology Distribution', fontsize=24)
    
    plt.tight_layout()

    # uncomment to save the plot
    #figure1.savefig('Numerology Histogram.png', dpi=250)
    
    return figure1

def figure_two():
    # set up the second figure
    figure2, (trend1, trend2) = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
    figure2.patch.set_facecolor('#d9d9d9')
    trend1.set_facecolor('#f5f0e8')
    trend2.set_facecolor('#f5f0e8')
    
    trend1.grid(True, color='#c9c9c9')
    trend2.grid(True, color='#c9c9c9')
    
    # create small subset of runs and note index
    small = simulation_summary.sample(n=77, random_state=808).sort_values('Run')
    small['Index'] = range(len(small))
    
    # plot the small subset
    trend1.plot(small['Index'], small['Average Numerology'], 
                alpha=0.8, color='#E67E50')
    trend1.fill_between(small['Index'], 
                      small['Average Numerology'] - small['Error Level'],
                      small['Average Numerology'] + small['Error Level'],
                      alpha=0.2, color='#F4A582', label='±1 SE')
    trend1.set_title('n = 77')
    trend1.set_ylabel('Average Numerology Value')
    trend1.legend(loc='upper right')
    
    # much larger subset and indices
    large = simulation_summary.sample(n=777, random_state=808).sort_values('Run')
    large['Index'] = range(len(large))
    
    # saving interquartile range for lines
    q25 = large['Average Numerology'].quantile(0.25)
    q75 = large['Average Numerology'].quantile(0.75)
    
    # comparison plot
    trend2.plot(large['Index'], large['Average Numerology'], 
                alpha=0.8, color='#E67E50')
    trend2.fill_between(large['Index'], 
                        large['Average Numerology'] - large['Error Level'],
                        large['Average Numerology'] + large['Error Level'],
                        alpha=0.2, color='#F4A582', label='±1 SE')
    
    # adding lines for IQR 
    trend2.axhline(q25, color='#3a3a4d', alpha=0.4, linestyle='--')
    trend2.axhline(q75, color='#3a3a4d', alpha=0.4, linestyle='--')
    trend2.set_title('n = 777 w/ IQR', fontsize=12)
    trend2.legend(loc='upper right')
    
    # full figure display
    figure2.suptitle('Trend of Average Numerology', fontsize=24)
    figure2.text(0.5, -0.1, 'Run Number', ha='center', fontsize=16)

    # uncomment to save the plot
    #figure2.savefig('Average Numerology Trend.png', dpi=250)
    
    return figure2

def figure_three():
    # initialize third figure
    figure3, (score1, score2) = plt.subplots(1, 2, figsize=(14, 5))
    
    figure3.patch.set_facecolor('#f5f0e8')
    score1.set_facecolor('#f5f0e8')
    score2.set_facecolor('#f5f0e8')
    
    score1.grid(True, color='#c9c9c9')
    score2.grid(True, color='#c9c9c9')

    small = simulation_summary.sample(n=77, random_state=808).sort_values('Run')
    small['Index'] = range(len(small))
    
    # plot the smaller sample's score trend
    sns.lineplot(data=small, x='Index', y='Positivity Score', 
                 alpha=0.7, color='#E67E50', ax=score1)
    
    score1.set_title('Smaller Subset')
    score1.set_xlabel('')
    score1.set_ylabel('Indicator Score')
    score1.tick_params(colors='white', labelsize=10)

    # much larger subset and indices
    large = simulation_summary.sample(n=777, random_state=808).sort_values('Run')
    large['Index'] = range(len(large))
    
    # plot the larger sample's score trend
    sns.lineplot(data=large, x='Index', y='Positivity Score', 
                 alpha=0.7, color='#E67E50', ax=score2)
    # add a line for the mean
    score2.axhline(large['Positivity Score'].mean(), color='#C1440E', 
                   alpha=0.8, linestyle='--')
    
    score2.set_title('Larger Subset w/ Mean')
    score2.set_xlabel('')
    score2.set_ylabel('')
    score2.yaxis.tick_right()
    
    # polish the figure
    figure3.suptitle('Valence Trend', fontsize=24)
    figure3.text(0.5, -0.01, 'Run Number', ha='center', fontsize=16)

    # uncomment to save the plot
    #figure3.savefig('Trend in Valence Assignment.png', dpi=250)
    
    return figure3

def figure_four():
    # initialize fourth figure
    figure4, (accuracy1, accuracy2) = plt.subplots(1, 2, figsize=(14, 5))
    figure4.patch.set_facecolor('#d9d9d9')
    accuracy1.set_facecolor('#f5f0e8')
    accuracy2.set_facecolor('#f5f0e8')
    
    accuracy1.grid(True, color='#c9c9c9')
    accuracy2.grid(True, color='#c9c9c9')
    
    # calculate the cumulative averages
    simulation_summary['Correct Rate'] = simulation_summary['Correct Guess'].expanding().mean()
    simulation_summary['Adjusted Rate'] = simulation_summary['Adjusted Guess'].expanding().mean()
    
    # look closer at the first 88 runs
    first_runs = simulation_summary.head(88)
    
    accuracy1.plot(first_runs['Run'], first_runs['Correct Rate'], 
             label='Read in Correct Position', color='#A23B72', linewidth=2)
    accuracy1.plot(first_runs['Run'], first_runs['Adjusted Rate'], 
             label='Score Adjusted for Confidence', color='#F18F01', linewidth=2)
    accuracy1.set_title('First 88 Runs')
    accuracy1.set_ylabel('Accuracy Rate')
    accuracy1.legend(loc='upper right', fontsize=8)
    
    # plot overall accuracy convergence
    accuracy2.plot(simulation_summary['Run'], simulation_summary['Correct Rate'], 
             label='Read in Correct Position', color='#A23B72', linewidth=2)
    accuracy2.plot(simulation_summary['Run'], simulation_summary['Adjusted Rate'], 
             label='Score Adjusted for Confidence', color='#F18F01', linewidth=2)
    accuracy2.set_title('Overall')
    accuracy2.legend(loc='upper right', fontsize=8)
    
    # you know the drill
    figure4.suptitle('Temporality Convergence Rate', fontsize=24)
    figure4.text(0.5, -0.1, 'Run Number', ha='center', fontsize=16)

    # uncomment to save the plot
    #figure4.savefig('Temporality Convergence Rates.png', dpi=250)
    
    return figure4

def figure_five(reading_history):
    
    # initialize elements tracker
    figure5, (element1, element2) = plt.subplots(1, 2, figsize=(14, 5))
    
    figure5.patch.set_facecolor('#d9d9d9')
    element1.set_facecolor('#f5f0e8')
    element2.set_facecolor('#f5f0e8')
    
    element1.set_axisbelow(True)
    element2.set_axisbelow(True)
    element1.grid(True, color='#c9c9c9')
    element2.grid(True, color='#c9c9c9')
    
    # assign colors to the elements and extract these from dataframes
    element_colors = {'Fire': '#A23B3F', 'Water': '#2E86AB', 'Air': '#D9D9D9', 'Earth': '#6B8E23'}
    
    # Use reading_history instead of simulation_summary
    reading_counts = reading_history['Element'].value_counts()
    deck_counts = cards['Element'].value_counts()
    
    # show distribution across all readings
    bars1 = element1.bar(reading_counts.index, reading_counts.values, 
                         color=[element_colors[e] for e in reading_counts.index], 
                         alpha=0.8)
    element1.set_title('Your Readings', fontsize=16)
    element1.set_ylabel('Count')
    
    # add count values for each bar
    for bar in bars1:
        height = bar.get_height()
        element1.text(bar.get_x() + bar.get_width()/2., height,
                 f'{int(height)}', ha='center', va='bottom')
    
    # compare to original distribution
    bars2 = element2.bar(deck_counts.index, deck_counts.values, 
                         color=[element_colors[e] for e in deck_counts.index], 
                         alpha=0.8)
    element2.set_title('Across Deck', fontsize=16)
    element2.set_ylabel('')
    element2.yaxis.tick_right()
    
    # adding count values
    for bar in bars2:
        height = bar.get_height()
        element2.text(bar.get_x() + bar.get_width()/2., height,
                 f'{int(height)}', ha='center', va='bottom')
    
    # add shared titles and display plots
    figure5.suptitle('Your Elemental Distribution', fontsize=24)
    figure5.text(0.5, 0.02, 'Elements', ha='center', fontsize=16)
    
    plt.tight_layout()
    return figure5

def figure_six(reading_history):
    astrologies = reading_history['Astrology']

    astrology_counts = Counter()
    
    for entry in astrologies:
        if pd.notna(entry):  # Skip NaN values
            # Split by comma and strip whitespace from each value
            values = [val.strip() for val in str(entry).split(',')]
            astrology_counts.update(values)
    
    wordcloud = WordCloud(width=800, height=400, 
                          background_color='#f5f0e8',
                          colormap='Oranges').generate_from_frequencies(astrology_counts)
    # Display the wordcloud
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Your Zodiac Chart', fontsize=16, pad=20)
    plt.tight_layout()
    plt.gcf().patch.set_facecolor('#d9d9d9')
    
    return plt