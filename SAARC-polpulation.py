import matplotlib.pyplot as plt
import main

def saarc_countries_population():
    data = main.read_csv('population-estimates_csv.csv')
    sarrc_countries = main.SAARC_COUNTRIES
    sarrc_population_dict = {}
    for row in data:
        if row['Region'] in sarrc_countries:
            year = row['Year']
            population = float(row['Population'])
            if year in sarrc_population_dict:
                sarrc_population_dict[year] += population
            else:
                sarrc_population_dict[year] = population
    
    def plot():
        year = sarrc_population_dict.keys()
        pop = sarrc_population_dict.values()
        plt.bar(year,pop)
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("SAARC countries population by each year")
        plt.xticks(rotation=90)
        plt.show()
    plot()

saarc_countries_population()