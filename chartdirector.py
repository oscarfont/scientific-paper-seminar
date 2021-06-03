import matplotlib.pyplot as plt
import json

class ChartDirector:
    def __init__(self):
        self.data = []
        self.labels = []

    def read_data_from_source(self, source, field):
        f = open(source)
        self.data = json.load(f)[field]
        f.close()

    def generate_random_labels(self,num_labels):
        for i in range(0,num_labels):
            self.labels.append(i)

    def export_bar_chart(self,output):
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(self.labels,self.data)
        #plt.show()
        plt.savefig(output+'foo.png')


# read data from source
chart_director = ChartDirector()
print('Reading data from source...')
chart_director.read_data_from_source('./data/numbers.json','numbers')
print('Data loaded!')
print('Generating words...')
chart_director.generate_random_labels(1000)
print('Words generated!')
print('Plotting Bar Chart...')
chart_director.export_bar_chart('./data/')
print('Bar Chart Plotted!')