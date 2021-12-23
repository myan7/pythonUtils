from pathlib import Path
import csv
import random
import numpy as np
from beans.attribute import Attribute

# create sample answer key, 50 records
ansKey = Path(Path.cwd()/"answerKey.csv")

# generate sample data


header = ['key', 'at01s', 'at02s', 'at03s', 'at04s', 'at05s', 'at06s', 'at07s', 'at08s', 'at09s']

# function of generating data
def generate_data(numofSub,headers,csvFile):
    values = []
    sub = 1
    while sub <= numofSub:
        value = []
        # add key
        value.append(sub)
        # add at01s - at03s
        for i in range(3):
            value.append(random.randint(6000,9999))
        # add at04s - at09s
        for i in range(6):
            value.append(random.random())
        values.append(value)
        sub += 1

    with open(csvFile,"w",newline='\n') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        for element in values:
            csv_writer.writerow(element)

# invoke generate_data function. comment out once executed.
# generate_data(10,header,ansKey)           

def csv_to_layout(csvfile):
    pass

# You should check for basestring instead of str
# since it's a common class
# from which both the str and unicode types inherit.
# Checking only the str leaves out the unicode types.
def checkType(obj):
    return bool(obj) and all(isinstance(e,basestring) for e in obj)

def getMax(l):
    return max( [float(x) for x in l[1:]])

def getMin(l):
    return min( [float(x) for x in l[1:]])

def getName(l):
    return l[0]

def getLength(maxVal):
    if int(maxVal) == maxVal:
        maxVal = int(maxVal)        
    length = len(str(maxVal))
    return length

def getType(maxVal):
    if int(maxVal) == maxVal:
        return "long"
    elif int(maxVal) != maxVal:
        return "double"

def getAttr(l):
    maxVal = getMax(l)
    minVal = getMin(l)
    name = getName(l)
    length = getLength(maxVal)
    dataType = getType(maxVal)
    attr = Attribute(name,maxVal,minVal,length,dataType)
    return attr
        
matrix = None    
# convert the data to a matrix transposed
with open(ansKey,"r") as file:
    reader = csv.reader(file,delimiter=",")
    temp = list(reader)
    matrix = np.array(temp).T

layout = []
for e in matrix:
    attr = getAttr(e)
    layout.append(attr.__str__())
    print(layout)
    
layoutFile = Path(Path.cwd()/"Layout.csv")
with open(layoutFile,"w",newline='\n') as file:
    csv_writer = csv.DictWriter(file,fieldnames=['name','maxVal','minVal','length','dataType'])
    csv_writer.writeheader()
    csv_writer.writerows(layout)
    
    
