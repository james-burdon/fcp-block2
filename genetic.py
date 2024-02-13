import sys
import csv
import math



filename = sys.argv[1]


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
    complement_seq = ''
    for character in seq:
        if character == 'a':
            newcharacter = 't'
        elif character == 't':
            newcharacter = 'a'
        elif character == 'c':
            newcharacter = 'g'
        else:  # does the last one
            newcharacter = 'c'
        complement_seq = complement_seq + newcharacter

    if reverse == True:
        complement_seq = complement_seq[::-1]

    return complement_seq

def test_rev_comp():
    assert complement('ATCG', True)=='CGAT', "reverse complement test"
    print("Tests passed")
    return

print(base_count(load_an_proc_data('sequence.fasta'), base_dict))

test_rev_comp()

print(complement(load_an_proc_data('sequence.fasta'), True))

