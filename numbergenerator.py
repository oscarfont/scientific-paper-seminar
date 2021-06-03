import random
import json

class NumberGenerator:
    def __init__(self, min_value, max_value, length):
        self.min_number = min_value
        self.max_number = max_value
        self.numbers_length = length
        self.numbers = []

    def generate_randomly(self):
        for i in range(0,self.numbers_length):
            n = (random.random()*self.max_number) - self.min_number
            self.numbers.append(n)

    def export_to_json(self,path):
        jsonOutput = {'numbers' : self.numbers}
        with open(path, 'w') as f:
            json.dump(jsonOutput, f, ensure_ascii=False, indent=4)


print('Generating random numbers...')
# generate 1000 random numbers from 0 to 100
number_generator = NumberGenerator(0,100,1000)
number_generator.generate_randomly()
print('Numbers generated!')
# export numbers to list
print('Exporting data...')
number_generator.export_to_json('./data/numbers.json')
print('Data exported!')