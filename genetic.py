import sys
import csv
import math


with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    dataold = list(reader)