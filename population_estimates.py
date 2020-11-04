import csv
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
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title("India - Population vs Year")
    plt.show()


def asean_plot(csv_read):
    x = []
    y = []
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
    for line in csv_read:
        if((line[0] in ASEAN) and (line[2] == "2014")):
            x.append(line[0])
            y.append(float(line[3]))
    plt.figure(figsize=(8, 4))
    plt.bar(x, y, width=0.4)
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.title("ASEAN - Countries vs Population")
    plt.show()


def saarc_plot(csv_read):
    d = {}
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
    for line in csv_read:
        if(line[0] in SAARC):
            if(line[2] in d):
                d[line[2]] += float(line[3])
            else:
                d[line[2]] = float(line[3])
    plt.figure(figsize=(14, 6))
    plt.bar(d.keys(), d.values(), label="SAARC")
    plt.xlabel('Year')
    plt.ylabel('Total Population')
    plt.title("SAARC - Total population vs Years")
    plt.xticks(rotation=90)
    plt.show()


if __name__ == "__main__":
    with open('/home/chris/Downloads/popest.csv', 'r') as newfile:
        csv_read = list(csv.reader(newfile, delimiter=','))
        india_plot(csv_read)
        asean_plot(csv_read)
        saarc_plot(csv_read)
