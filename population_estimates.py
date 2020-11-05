import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def india_plot(csv_read):
    # function to plot the year vs poplation for India

    x = []
    y = []

    for line in csv_read:
        if(line[0] == "India"):
            x.append(int(line[2]))
            y.append(float(line[3]))

    # plotting graph
    plt.bar(x, y)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("India - Year vs Population")
    plt.tight_layout()
    plt.show()


def asean_plot(csv_read, asean):
    # function to plot the bar graph of population of asean nations

    x = []
    y = []

    for line in csv_read:
        if((line[0] in asean) and (line[2] == "2014")):
            x.append(line[0])
            y.append(float(line[3]))

    # plotting the graph
    plt.figure(figsize=(8, 4))
    plt.bar(x, y, width=0.4)
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.title("ASEAN - Country vs Population")
    plt.tight_layout()
    plt.show()


def saarc_plot(csv_read, saarc):
    # function to plot the total population of SAARC nations

    yearwise_pop = {}

    # creates a dictionary of total population for each year
    for line in csv_read:
        if(line[0] in saarc):
            if(line[2] in yearwise_pop):
                yearwise_pop[line[2]] += float(line[3])
            else:
                yearwise_pop[line[2]] = float(line[3])

    # plotting bar graph
    plt.figure(figsize=(14, 6))
    plt.bar(yearwise_pop.keys(), yearwise_pop.values())
    plt.xlabel("Year")
    plt.ylabel("Total Population")
    plt.title("SAARC - Year vs Total population")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def group_plot_asean(csv_read, asean):
    # function to create group plot for ASEAN countries

    population = {}
    years = [str(i) for i in range(2004, 2015)]
    x = np.arange(len(years))
    bar_width = 0.1
    fig = plt.figure(figsize=(12, 6))
    ax = plt.subplot()
    rects = [x]

    # loop through the year and creates a dictionary of countrywise population
    for i, year in enumerate(years):
        for line in csv_read:
            if(line[2] == year and line[0] in asean):
                if(line[0] in population):
                    population[line[0]].append(float(line[3]))
                else:
                    population[line[0]] = [float(line[3])]

    # creates a bar plot for each country
    for i, j in enumerate(population.keys()):
        rects.append(ax.bar(x+bar_width*i,
                            population[j],
                            width=bar_width,
                            label=j
                            ))

    # plotting the graph
    ax.set_xticks(x+bar_width*i/2)
    ax.set_title("Year vs Population for each ASEAN nation")
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
        "Vietnam"
        ]

    # opening the csv file and writing to a list
    with open('/home/chris/Downloads/popest.csv', 'r') as newfile:
        csv_read = list(csv.reader(newfile, delimiter=','))

        # making function calls to plot the required graphs
        plt.figure(figsize=(10, 6))
        india_plot(csv_read)
        asean_plot(csv_read, asean)
        saarc_plot(csv_read, saarc)
        group_plot_asean(csv_read, asean)
