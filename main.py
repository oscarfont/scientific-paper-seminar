from numbergenerator import NumberGenerator
from chartdirector import ChartDirector

print('Generating random numbers...')
# generate 1000 random numbers from 0 to 100
number_generator = NumberGenerator(0,100,1000)
number_generator.generate_randomly()
print('Numbers generated!')
# export numbers to list
print('Exporting data...')
number_generator.export_to_json('./data/numbers.json')
print('Data exported!')

# read data from source
chart_director = ChartDirector()
print('Reading data from source...')
chart_director.read_data_from_source('./data/numbers.json','numbers')
print('Data loaded!')
print('Generating words...')
chart_director.generate_random_labels(1000)
print('Words generated!')
print('Plotting Bar Chart...')
chart_director.plot_bar_chart()
print('Bar Chart Plotted!')