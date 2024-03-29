import sys
import csv
import math

filename = 'sequence.fasta' #sys.argv[1]


def load_an_proc_data(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
    return data


base_dict = {'a': 0, 'c': 0, 't': 0, 'g': 0}


def base_count(data, base_dict):
    new_base_dict = base_dict.copy()
    for i in range(len(data)):
        new_base_dict['{}'.format(data[i])] += 1
    return new_base_dict


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
    assert complement('ATCG') == 'TAGC', "complement test"
    assert complement('ATCG', True) == 'CGAT', "reverse complement test"
    print("Tests passed")


def gc_count(dict):
    GC = (dict['g'] + dict['c']) / (dict['g'] + dict['c'] + dict['a'] + dict['t']) * 100
    return GC


def test_gc_content():
    assert gc_count(base_count('ggggaaaaaaaatttatatatcgcc', base_dict)) == 0.32, "gc_content test"
    print("Tests passed")


def mean_gc_content(sequence, window_size):
    list_of_islands = detect_cpg_islands(sequence, window_size, 0)
    total = 0
    for i in range(len(list_of_islands)):
        total += gc_count(base_count(list_of_islands['{}'.format(i)], base_dict))
    mean_value = total / len(list_of_islands)
    return mean_value


def detect_cpg_islands(sequence, window_size, gc_threshold):
    cpg_islands = {}
    for i in range(len(sequence) - window_size + 1):
        if gc_count(base_count(sequence[i:i + window_size], base_dict)) > gc_threshold:
            cpg_islands['{}'.format(i)] = sequence[i:i + window_size]
    return cpg_islands


def main(infile, window_size=200, gc_multiplier=2):
    seq = load_an_proc_data(infile)
    cpg_islands = detect_cpg_islands(seq, window_size, (gc_multiplier * mean_gc_content(seq, window_size)))
    # print("GC Islands:")
    cpg_island_output_list = []
    for index_key, value in cpg_islands.items():
        cpg_island_output_list.append(
            f"{infile}: Start: {index_key}, End: {int(index_key) + window_size - 1}, GC Content: {gc_count(base_count(value, base_dict)):.2f}%")
    return cpg_island_output_list


flags = ['--input', '--output', '--base-count', '--reverse-complement', '--GC-content', '--number-of-islands']


def input():
    if '--input' in sys.argv:
        assert sys.argv[sys.argv.index('--input') + 1] not in flags, "Please give an input file"
        increment = 1
        Files = []
        while sys.argv[sys.argv.index('--input') + increment] not in flags:
            Files += [sys.argv[sys.argv.index('--input') + increment]]
            increment += 1
    return Files


def output():
    if '--output' in sys.argv:
        assert sys.argv[sys.argv.index('--output') + 1] not in flags, "Please give an output filename"
        outfile_name = sys.argv[sys.argv.index('--output') + 1]
        return outfile_name
    else:
        return False


def base_count_call(Files):
    base_count_list = []
    for file in Files:
        base_count_list.append(base_count(file, base_dict))
    return base_count_list


def reverse_complement(Files):
    reverse_list = []
    for file in Files:
        reverse_list.append(complement(file, True)[:50])
    return reverse_list


# main(filename,100,49)


def GC_content(raw_Files, window_size, gc_multiplier, stuck=False):
    gc_content_list = []
    if stuck == True:
        for raw_file in raw_Files:
            window_size = len(load_an_proc_data(raw_file))
            gc_content_list.append(main(raw_file, window_size, gc_multiplier))
    else:
        for raw_file in raw_Files:
            gc_content_list.append(main(raw_file, window_size, gc_multiplier))
    return gc_content_list


def number_of_islands(raw_Files, window_size, gc_multiplier):
    list_of_island_stats = []
    for i, elem in enumerate(GC_content(raw_Files, window_size, gc_multiplier)):
        list_of_island_stats.append(f"Input file number: {i + 1}, Number of islands: {len(elem)}")
    return list_of_island_stats


def report():

    raw_Files = input()
    # this processes the raw inputted file data
    Files = []
    for raw_file in raw_Files:
        Files.append(load_an_proc_data(raw_file))

    list_of_all_things = []

    # either to be printed to terminal or saved to file...
    if '--base-count' in sys.argv:
        list_of_all_things.append(base_count_call(Files))
    if '--reverse-complement' in sys.argv:
        list_of_all_things.append(reverse_complement(Files))
    if '--GC-content' in sys.argv :
        list_of_all_things.append(GC_content(input(), 150, 0, True))
    if '--number-of-islands' in sys.argv:
        list_of_all_things.append(number_of_islands(input(), 150, 1.4))

    if output() != False:
        outfile_name = output()
        with open(f'{outfile_name}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(list_of_all_things)
    else:
        print(list_of_all_things)

    return


report()
# print(base_count(load_an_proc_data(filename),base_dict))
# for file in input():
#     print(base_count_call(load_an_proc_data(file),base_dict))
