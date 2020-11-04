import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
plt.autoscale(enable=True, axis='both', tight=None)


def india_plot(csv_read):
    x = []
    y = []
    for line in csv_read:
        if(line[0] == "India"):
            x.append(int(line[2]))
            y.append(float(line[3]))
    plt.bar(x, y)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("India - Population vs Year")
    plt.show()


def asean_plot(csv_read, ASEAN):
    x = []
    y = []
    for line in csv_read:
        if((line[0] in ASEAN) and (line[2] == "2014")):
            x.append(line[0])
            y.append(float(line[3]))
    plt.figure(figsize=(8, 4))
    plt.bar(x, y, width=0.4)
    plt.xlabel("Country")
    plt.ylabel("Population")
    plt.title("ASEAN - Countries vs Population")
    plt.show()
    return ASEAN


def saarc_plot(csv_read, SAARC):
    yearwise_pop = {}
    for line in csv_read:
        if(line[0] in SAARC):
            if(line[2] in yearwise_pop):
                yearwise_pop[line[2]] += float(line[3])
            else:
                yearwise_pop[line[2]] = float(line[3])
    plt.figure(figsize=(14, 6))
    plt.bar(yearwise_pop.keys(), yearwise_pop.values(), label="SAARC")
    plt.xlabel('Year')
    plt.ylabel('Total Population')
    plt.title("SAARC - Total population vs Years")
    plt.xticks(rotation=90)
    plt.show()


def group_plot_asean(csv_read, ASEAN):
    population = {}
    years = ["2009", "2010", "2011", "2012", "2013", "2014"]
    x = np.arange(len(years))
    bwidth = 0.1
    fig, ax = plt.subplots()
    rects = [x]
    for i, year in enumerate(years):
        for line in csv_read:
            if(line[2] == year and line[0] in ASEAN):
                if(line[0] in population):
                    population[line[0]].append(float(line[3]))
                else:
                    population[line[0]]=[float(line[3])]
    for i, j in enumerate(population.keys()):
        rects.append(ax.bar(x+bwidth*i, population[j], width=bwidth, label=j))
    ax.set_xticks(x)
    ax.set_title("Population vs Year for each ASEAN nation")
    ax.set_xlabel("Years")
    ax.set_ylabel("Population")
    ax.set_xticklabels(years)
    ax.legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    SAARC = [
             "Afghanistan",
             "Bangladesh",
             "Bhutan",
             "India",
             "Maldives",
             "Nepal",
             "Pakistan",
             "Sri Lanka"
             ]
    ASEAN = [
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
    with open('/home/chris/Downloads/popest.csv', 'r') as newfile:
        csv_read = list(csv.reader(newfile, delimiter=','))
        india_plot(csv_read)
        asean_plot(csv_read, ASEAN)
        saarc_plot(csv_read, SAARC)
        group_plot_asean(csv_read, ASEAN)
