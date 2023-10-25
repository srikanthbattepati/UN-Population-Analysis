import matplotlib.pyplot as plt
import main

def india_population_over_years():
    data = main.read_csv('population-estimates_csv.csv')
    india_population_dict = {}
    for row in data:
        if row['Region'] == 'India':
            india_population_dict[row['Year']] = row['Population']

    def plot():
        year = india_population_dict.keys()
        population = india_population_dict.values()
        plt.bar(year,population)
        plt.xlabel("year")
        plt.ylabel("population")
        plt.title("Indian population in each year")
        plt.xticks(rotation = 90)
        plt.show()
    plot()

india_population_over_years()