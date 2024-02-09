import sys
import csv
import math

def load_an_proc_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=' ')
        dataold = list(reader)


data = [[val for val in sublist if len(val)>0] for sublist in dataold]

numdata = [[float(val) if val.isnumeric() else  val for val in sublist] for sublist in data[7:]]

print(numdata)

def annual_average(numdata):
    Average=[]
    temperaturemax,temperaturemin,rainfall=[],[],[]
    temperaturemax.append(numdata[0][2])
    temperaturemin.append(numdata[0][3])
    rainfall.append(float(''.join([i for i in numdate[0][6] if i.isdigit()])))
    for i in range(1,len(numdata)):
     if numdata[i][0]==numdata[i-1][0]:
         temperaturemax.append(numdata[i][2])
         temperaturemin.append(numdata[i][3])
         rainfall.append(numdate[i][5])
     else:
         Average+=[numdata[i-1][0],max(temperaturemax),min(temperaturemin),sum(rainfall)/len(rainfall)]
         temperaturemax,temperaturemin,rainfall=[],[],[]
    return Average 

print(annual_average(numdata))










        

