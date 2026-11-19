# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


# load Provo River streamflow data
data = np.genfromtxt(
    'June-2021-Provo-River-Streamflow-Rates.csv',
    delimiter=',',
    dtype=str,
    skip_header=1
) # commas separate the columns, and the first row is skipped

# slice the array into columns
x = data[:, 0] # select the date column for the x-axis
# each additional column represents water flow measured at a different monitoring site; converts the values to floats so they can be graphed
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

import matplotlib.dates as mdates
import datetime as dt

# convert date strings into datetime objects
dates = [dt.datetime.strptime(d.strip(), '%Y-%m-%d %H:%M:%S') for d in x] # this CSV includes a time such as 00:00:00 so this needs to be converted to hour, minute, seconds

plt.figure(figsize=(8, 5)) # create an 8in by 5in figure

# plot the flowrate of each monitoring site, each site is drawn as a separate line; labels allow us to identify sites in the legend
plt.plot(dates, y_1, label='10163000')
plt.plot(dates, y_2, label='10155200')
plt.plot(dates, y_3, label='10155500')
plt.plot(dates, y_4, label='10154200')
plt.plot(dates, y_5, label='10155000')

plt.title('Provo River Streamflow Data (2021)') # add a graph title describing the dataset
plt.xlabel('Date') # label the horizontal axis with dates
plt.ylabel('Flowrate (cfs)') # label the vertical axis with the measurement units with cfs standing for cubic feet per second

plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4)) # place major x-axis tick marks every four days
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) # display dates in year-month-day format

plt.legend(title='Site Numbers') # create a legend with the title "Site Numbers"
plt.grid(True) # add gridlines for comparing flowrates

plt.xticks(rotation=45) # rotate date labels 45 degrees to prevent overlap

plt.tight_layout() # adjust spacing and display the graph
plt.show()