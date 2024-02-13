import sys
import csv
import math


#filename = sys.argv[1]

def load_an_proc_data(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    return data

base = {'a': 0, 'c': 0, 't': 0, 'g': 0}


def base_count(data,base):
    for i in range(len(data)):
        base['{}'.format(data[i])] += 1
    return base

# for key, value in base.items():
#     base[key] = value + 1
base_count(load_an_proc_data('sequence.fasta'),base)