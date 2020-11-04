# dataproject-python

# Analytics on UN Population


## Objective
To convert raw open data, country and year wise population estimates in this case, into charts that tell some kind of story.

## Data and References

[click here](https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv) to download the csv data

[ASEAN countries wiki](https://en.wikipedia.org/wiki/ASEAN)

[SAARC countries wiki](https://en.wikipedia.org/wiki/South_Asian_Association_for_Regional_Cooperation)

## Dependancies

The Dependancies required for running the program has been provided in the requirements.txt file

## code contents

1) imported modules -> csv, numpy, matplotlib
2) functions used -> india_plot, asean_plot, saarc_plot, group_plot_asean, main

## Running the program

Running the program returns 4 graphs which are solutions to the 4 problem statements

1. Bar plot of **Population of India** vs **Year**
2. Bar plot of **Population of ASEAN countries**
   * Gives the population of each ASEAN country vs Year
   * Data considered for the year **2014**
3) Bar plot of **Total Population of SAARC Countries**
4) Grouped bar chart of **ASEAN Population**
   * Shows the grouped bar chart for each ASEAN countries
   * Graph is ordered into groups by year from **2009 to 2014**
