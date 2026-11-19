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

def summarize(dates, flows, sites):
    """Calculate streamflow statistics and save a CSV report."""

    # create the CSV file
    with open("streamflow_summary.csv", "w") as file:

        # write column headings to the CSV
        file.write("Gauge,Max (cfs),Date of Max,Min (cfs),Avg (cfs)\n")

        # print table headings in the terminal
        print(f"{'Gauge':<12}{'Max (cfs):>12'}"
              f"{'Date of Max':>20}{'Min (cfs)':>12}{'Avg (cfs)':>12}")

       # calculate statistics for each monitoring station
        for i in range(len(sites)):
            values = flows[:, i]

            max_flow = np.max(values)
            min_flow = np.min(values)
            avg_flow = np.mean(values)

            # find when the maximum flow occurred
            max_index = np.argmax(values)
            max_date = dates[max_index].strftime('%Y-%m-%d %H:%M')

            # display results in the terminal
            print(f"{sites[i]:<12}{max_flow:>12.2f}"
                  f"{max_date:>20}{min_flow:>12.2f}{avg_flow:>12.2f}")

            # save results to the CSV
            file.write(f"{sites[i]},{max_flow:.1f},{max_date},"
                       f"{min_flow:.1f},{avg_flow:.1f}\n"
                       )

# The main program calls the functions to load, plot, and summarize the streamflow data. 
# Main program
sites = ["10163000", "10155200", "10155500",
         "10154200", "10155000"]

dates, flows = load_streamflow(
    "June-2021-Provo-River-Streamflow-Rates.csv"
    )

plot_streamflow(dates, flows, sites)
# values for gauge 10163000: max= 131, avg = 56.95
summarize(dates, flows, sites)

def threshold_report(flows, sites):
    """Report hours each gauge exceeded a user-entered flow threshold."""

    # Ask the user to enter a threshold in cubic feet per second
    threshold = float(input("Enter a flow threshold (cfs): "))

    print("\nHours above threshold:")

    # Check each monitoring station
    for i in range(len(sites)):

        # Compare each flow reading with the threshold
        above = flows[:, i] > threshold

        # Count readings above the threshold and convert to hours
        hours = np.sum(above) * 0.25

        # Print results for this gauge
        print(f"Gauge {sites[i]}: {hours:.2f} hours")

threshold_report(flows, sites)