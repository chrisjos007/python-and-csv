import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict
matplotlib.use('TkAgg')


def graph_plotter(x, y, x_label, y_label, title, rot=0):
    plt.bar(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if rot != 0:
        plt.xticks(rotation=rot)
    plt.tight_layout()
    plt.show()


def india_plot(csv_read):
    """ returns the plot of the indian population for each year """

    x = []
    y = []

    # creating x and y coordinates
    for line in csv_read:
        if line[0] == "India":
            x.append(int(line[2]))
            y.append(float(line[3]))

    # plotting the graph
    plt.figure(figsize=(10, 6))
    graph_plotter(
                 x, y, "Year", "Population",
                 "Year vs Population for India"
                 )


def asean_plot(csv_read, asean):
    """Returns a plot of the population of asean nations for 2014"""

    x = []
    y = []

    # creating x and y coordinates
    for line in csv_read:
        if (line[0] in asean) and (line[2] == "2014"):
            x.append(line[0])
            y.append(float(line[3]))

    # plotting the graph
    plt.figure(figsize=(12, 8))
    graph_plotter(
                  x, y, "Country", "Population",
                  "Country vs Population for ASEAN nations for 2014"
                  )


def saarc_plot(csv_read, saarc):
    """ Returns a plot the total population of SAARC nations """

    yearwise_pop = defaultdict(float)

    # creates a dictionary of total population for each year
    for line in csv_read:
        if line[0] in saarc:
            yearwise_pop[line[2]] += float(line[3])

    # plotting bar graph
    plt.figure(figsize=(14, 6))
    graph_plotter(
                 yearwise_pop.keys(), yearwise_pop.values(),
                 "Year", "Total Population",
                 "Year vs Total population for SAARC nations", 90
                 )


def group_plot_asean(csv_read, asean):
    """ Returns a group plot for ASEAN countries

    Grouped into countries over the years 2004 to 2014"""

    population = defaultdict(list)
    years = [str(i) for i in range(2004, 2015)]    # list of years
    x = np.arange(len(years))
    bar_width = 0.08
    fig = plt.figure(figsize=(12, 6))
    ax = plt.subplot()
    rects = [x]

    # loop through the year and creates a dictionary of countrywise population
    for year in years:
        for line in csv_read:
            if (line[2] == year) and (line[0] in asean):
                population[line[0]].append(float(line[3]))

    # creates a bar plot for each country
    for i, j in enumerate(population.keys()):
        rects.append(ax.bar(x+bar_width*i,
                            population[j],
                            width=bar_width,
                            label=j
                            ))

    # plotting the graph
    ax.set_xticks(x+bar_width*i/2)
    ax.set_title("Year vs Population for each ASEAN nation from 2004 to 2014")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")
    ax.set_xticklabels(years)
    ax.legend(
        loc='lower left',
        bbox_to_anchor=(0.0, 1.01),
        borderaxespad=0,
        frameon=False
        )
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    """Read in the csv file and create a list from it.

    Using the list, make function calls

    Function calls represent the solution plots"""

    # list of SAARC nations
    saarc = [
        "Afghanistan",
        "Bangladesh",
        "Bhutan",
        "India",
        "Maldives",
        "Nepal",
        "Pakistan",
        "Sri Lanka"
        ]

    # list of ASEAN nations
    asean = [
        "Singapore",
        "Brunei",
        "Malaysia",
        "Thailand",
        "Cambodia",
        "Indonesia",
        "Laos",
        "Myanmar",
        "Philippines",
        "Viet Nam"
        ]

    # opening the csv file and writing to a list
    with open('population-estimates_csv.csv', 'r') as newfile:
        csv_read = list(csv.reader(newfile, delimiter=','))

    # rename 2 nations to their shorter names
    for line in csv_read:
        if(line[0] == "Lao People's Democratic Republic"):
            line[0] = "Laos"
        if(line[0] == "Brunei Darussalam"):
            line[0] = "Brunei"

    # making function calls to plot the required graphs
    matplotlib.rcParams['axes.linewidth'] = 0.3
    india_plot(csv_read)
    asean_plot(csv_read, asean)
    saarc_plot(csv_read, saarc)
    group_plot_asean(csv_read, asean)
