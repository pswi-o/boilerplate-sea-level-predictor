# Sea Level Predictor
# Author: Pawel
# Date: April 2025
# Description: This script analyzes and predicts the rise of sea levels based on historical data.

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (for all data)
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    plt.plot(years_extended, slope_all * years_extended + intercept_all, label='Best fit: all data', color='blue')

    # Create second line of best fit (for data from 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, slope_recent * years_recent + intercept_recent, label='Best fit: from 2000', color='red')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    #plt.show()
    # Save plot and return for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()