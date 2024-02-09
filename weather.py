import sys
import csv
import math

with open('somewhere_better.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    dataold = list(reader)



# for i in range(dataold):
#     for index, val in enumerate(dataold[i]):
#         if val == '':
#             del(dataold[i][index])



data = [[val for val in sublist if len(val)>0] for sublist in dataold]

numdata = [[float(val) if val.isnumeric()==True else val for val in sublist] for sublist in data[7:]]

print(numdata)

def annual_average(numdata):
    for i in range(len(numdata)):
        temperature,rain=[],[]
        if numdata[i] not in year and len(year)=0:
            
