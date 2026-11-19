# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt

# Function 1:load and organize Provo River streamflow data
def load_streamflow(filename):
    """Read the streamflow CSV and return dates and flow values."""

    # load Provo River streamflow data
    data = np.genfromtxt(
        filename,
        delimiter=',',
        dtype=str,
        skip_header=1
    ) 

    # slice the array into columns
    x = data[:, 0] 

    # convert date strings into datetime objects
    dates = [
        dt.datetime.strptime(d.strip(), '%Y-%m-%d %H:%M:%S') 
        for d in x
    ]

    # select all five flow columns and convert to numbers
    flows = data[:, 1:6].astype(float)

    return dates, flows

# Function 2: plot the streamflow data
def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge."""

    plt.figure(figsize=(8, 5)) 

    # plot each monitoring site
    for i in range(len(sites)):
        plt.plot(dates, flows[:, i], label=sites[i])

    plt.title('Provo River Streamflow Data (2021)') 
    plt.xlabel('Date') 
    plt.ylabel('Flowrate (cfs)') 

    # format the dates on the x-axis 
    plt.gca().xaxis.set_major_locator(
        mdates.DayLocator(interval=4)
        )
    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter('%Y-%m-%d')
        ) # display dates in year-month-day format

    plt.legend(title='Site Numbers') 
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches='tight')
    plt.show()

# Main program
sites = ["10163000", "10155200", "10155500",
         "10154200", "10155000"]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
    )

plot_streamflow(dates, flows, sites)