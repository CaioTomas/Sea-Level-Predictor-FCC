import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    #Do the regressions
    x_f = df['Year']
    y_f = df['CSIRO Adjusted Sea Level']
    
    res_f = linregress(x_f, y_f)
    slope_f, intercept_f = (res_f[0], res_f[1]) #slope and y-intercept of the linear regression using the sea level from 1880 to 2013

    df2 = df.iloc[120:134,:] #dataframe of sea level from 2000 to 2013

    x_sec = df2['Year']
    y_sec = df2['CSIRO Adjusted Sea Level']

    res_sec = linregress(x_sec, y_sec)
    slope_sec, intercept_sec = (res_sec[0], res_sec[1]) #slope and y-intercept of the linear regression using the sea level from 2000 to 2013
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15,5))

    ax =  df.plot(x ='Year', y='CSIRO Adjusted Sea Level', kind='scatter')

    # Create first line of best fit
    years_first = [i for i in range(1880, 2051)]
    bfline1_values = [slope_f * i + intercept_f for i in years_first]
    ax.plot(years_first, bfline1_values, 'b', color='red')

    # Create second line of best fit
    years_sec = [i for i in range(2000, 2051)]
    bfline2_values = [slope_sec * i + intercept_sec for i in years_sec]
    ax.plot(years_sec, bfline2_values, 'b', color='green')
    
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()