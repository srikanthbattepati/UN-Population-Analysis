from main import ASEAN_COUNTRIES, population_data, color_codes
import matplotlib.pyplot as plt
import numpy as np


def asean_population_by_year():
    data = main.load_csv('population-estimates_csv.csv')
    asean_countries = main.ASEAN_COUNTRIES
    color_codes = main.color_codes
    asean_year_population_dict = {}
    
    
    
    for row in data:
        if row['Year'] >= '2004' and row['Year'] <= '2014' and row['Region'] in ASEAN_COUNTRIES :
            if row['Year'] in asean_year_population_dict:
                asean_year_population_dict[row['Year']][row['Region']] = float(row['Population'])
            else:
                asean_year_population_dict[row['Year']] = {row['Region'] : float(row['Population'])}
    
    
    population = {}

    years  = [year for year in asean_year_population_dict]
    for country in ASEAN_COUNTRIES:
        population[country] = []
        for year in years:
            if asean_year_population_dict[year][country]:
                population[country].append(asean_year_population_dict[year][country])
            else:
                population[country].append(0)
    
    def plot():
        width = 0.2
        x = range(len(years))
        
        for index, country in enumerate(ASEAN_COUNTRIES):
            plt.bar(
                [pos + index * width for pos in x],
                population[country],
                label=country,
                width=width,
                color = color_codes[index]
                )
            plt.legend()
            plt.xticks([pos + 2 * width for pos in x], years)
        plt.show()
    plot()
    
asean_population_by_year()
     