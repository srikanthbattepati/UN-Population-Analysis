""" asean countries population in year 2014"""
import matplotlib.pyplot as plt
import main

def asean_countries_population():
    
    data = main.read_csv('population-estimates_csv.csv')
    asean_countires = main.ASEAN_COUNTRIES
    asean_population_dict = {}

    for row in data:
        if row['Year'] == '2014' and row['Region'] in asean_countires:
            asean_population_dict[row['Region']] = row['Population']
    
    def plot():
        year = asean_population_dict.keys()
        pop = asean_population_dict.values()
        plt.bar(year,pop)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("ASEAN countries population by each year")
        plt.show()
    plot()

asean_countries_population()