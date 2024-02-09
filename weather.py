import sys
import csv
import math

def load_an_proc_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        dataold = list(reader)

    data = [[val for val in sublist if len(val)>0] for sublist in dataold]
    numdata = [[float(val) if val.replace('.','').isnumeric() else math.nan for val in sublist] for sublist in data if not any(map(lambda x : x.isalpha(),sublist))]
    return numdata

numdata = load_an_proc_data('somewhere_better.txt')

