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
    assert complement('ATCG')=='TAGC', "complement test"
    assert complement('ATCG', True)=='CGAT', "reverse complement test"
    print("Tests passed")

def gc_count(dict):
    GC=(dict['g']+dict['c'])/(dict['g']+dict['c']+dict['a']+dict['t'])*100
    return GC

def test_gc_content():
    assert gc_count(base_count('ggggaaaaaaaatttatatatcgcc',base_dict))==0.32, "gc_content test"
    print("Tests passed")

def detect_cpg_islands(sequence, window_size, gc_threshold):
    cpg_islands = []
    for i in range(len(sequence)-window_size+1):
        if gc_count(base_count(sequence[i:i+window_size],base_dict))>gc_threshold:
            cpg_islands.append(sequence[i:i+window_size])
    return cpg_islands

def main(infile):
    seq = load_an_proc_data(infile)
    cpg_islands = detect_cpg_islands(seq, window_size=200, gc_threshold=50.0)

    print("GC Islands:")
    for start, end, gc_count in cpg_islands:
        print(f"Start: {start}, End: {end}, GC Content: {gc_count:.2f}%")

main(filename)




#print(gc_count(base_count(load_an_proc_data(filename),base_dict)))
