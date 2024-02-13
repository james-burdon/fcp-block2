import sys
import csv
import math


# filename = sys.argv[1]

def load_an_proc_data(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    return data


base_dict = {'a': 0, 'c': 0, 't': 0, 'g': 0}


def base_count(data, base_dict):
    for i in range(len(data)):
        base_dict['{}'.format(data[i])] += 1
    return base_dict


# In DNA, the complementary base pairs are adenine (A) with thymine (T); and
# cytosine (C) with guanine (G)

def complement(seq, reverse=False):
    for character in seq:
        if character == 'a':
            character = 't'
        elif character == 't':
            character = 'a'
        elif character == 'c':
            character = 'g'
        else:  # does the last one
            character = 'c'

    if reverse == True:
        seq = seq[::-1]

    return seq


print(base_count(load_an_proc_data('sequence.fasta'), base_dict))

print(complement(load_an_proc_data('sequence.fasta'),True))