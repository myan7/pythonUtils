from pathlib import Path
import csv
import random
import numpy as np
from beans.attribute import Attribute
import string

def random_string(letter_count, digit_count):  
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) # it converts the string to list.  
    random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
    final_string = ''.join(sam_list)  
    return final_string  



# function definitions

# function of generating data
def generate_data(numofSub,headers,csvFile):
    values = []
    sub = 1
    while sub <= numofSub:
        value = []
        
        # add key
        value.append(sub)
        # add at01s - at03s all integers
        for i in range(3):
            value.append(random.randint(6000,9999))
        # add at04s - at08s all doubles
        for i in range(5):
            value.append(random.random())

        # add at09s all string
        for i in range(1):
            value.append(random_string(7,2))
            
        values.append(value)
        sub += 1

    # write generated data into a csv file.
    with open(csvFile,"w",newline='\n') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        for element in values:
            csv_writer.writerow(element)


# You should check for basestring instead of str
# since it's a common class
# from which both the str and unicode types inherit.
# Checking only the str leaves out the unicode types.

# The builtin basestring abstract type was removed. Use str instead.
# The str and bytes types don’t have functionality enough in common to warrant a shared base class.
# The 2to3 tool (see below) replaces every occurrence of basestring with str.


"""
# just to fit python 2.X environment:
try:
  basestring
except NameError:
  basestring = str

  
def contains(l,typ):
    return any(isinstance(e, typ) for e in l)

def checkType(obj):
    return bool(obj) and all(isinstance(e,str) for e in obj)
    
def getPrecision(maxVal):
    precision = 0
    if int(maxVal) != maxVal:
        precision = 6
    elif isinstance(maxVal,str):
        precision = ''
    elif int(maxVal) == maxVal:
        precision = ''
    return precision


def getType0(maxVal):
    if int(maxVal) == maxVal:
        return "long"
    elif int(maxVal) != maxVal:
        return "double"
    elif isinstance(maxVal,str):
        return "char"

def getAttr0(l):
    maxVal = getMax(l)
    minVal = getMin(l)
    name = getName(l)
    length = getLength(maxVal)
    dataType = getType(maxVal)
    precision = getPrecision(maxVal)
    attr = Attribute(name,maxVal,minVal,length,dataType,precision)
    return attr


lst = ['1','2','1.23','']
print(getType2(lst))
    
"""

def getName(l):
    return l[0]

def getMax(l,dataType,precision):
    if dataType == "double":
        return max( [round(float(x),precision) for x in l])
    elif dataType == "long":
        return max([int(x) for x in l])
    elif dataType == "char":
        return max(l)

def getMin(l,dataType,precision):
    if dataType == "double":
        return min( [round(float(x),precision) for x in l])
    elif dataType == "long":
        return min([int(x) for x in l])
    elif dataType == "char":
        return min(l)

def getLength(maxVal,dataType,precision):
     
    if dataType == "char":
        length = len(maxVal)
    else:
        temp = 0 if precision == '' else precision + 1
        length = len(str(int(maxVal))) + temp
    return length

def getType(lst):
# lst doesn't have attrName and blanks
# determine type of the list
    try:
        tempList = [float(e) for e in lst]
        if all(int(e) == e for e in tempList):
            return "long"
        elif any(int(e) != e for e in tempList ):
            return "double"
    except ValueError:
        return "char"

def getAttr(lst):
    name = lst[0]
    valueList = lst[1:]
    # get rid of all blanks in a list
    cleanList = [x for x in valueList if x ]

    dataType = getType(cleanList)
    precision = 6 if dataType == "double" else ''
    
    maxVal = getMax(cleanList,dataType,precision)
    minVal = getMin(cleanList,dataType,precision)
    length = getLength(maxVal,dataType,precision)
    
    attr = Attribute(name,maxVal,minVal,length,dataType,precision)
    return attr    
    
# function getAttr requires that answerkey has header to get the name.
# think about how many data types do we have in our system
# 1 long, 2 double 3 char


            

def csv_to_layout(csvfile,layoutFile):
    matrix = None    
    # convert the data to a matrix transposed
    with open(csvfile,"r") as file:
        reader = csv.reader(file,delimiter=",")
        temp = list(reader)
        matrix = np.array(temp).T

    layout = []
    for e in matrix:
        attr = getAttr(e)
        layout.append(attr.__str__())
    
    with open(layoutFile,"w",newline='\n') as file:
        csv_writer = csv.DictWriter(file,fieldnames=['name','maxVal','minVal','length','dataType','precision'])
        csv_writer.writeheader()
        csv_writer.writerows(layout)


# generate sample data

header = ['key', 'at01s', 'at02s', 'at03s', 'at04s', 'at05s', 'at06s', 'at07s', 'at08s', 'at09s']

ansKey = Path(Path.cwd()/"answerKey.csv")

# invoke generate_data function. comment out once executed.
# create sample answer key, 100 records
generate_data(100,header,ansKey)               
    
layoutFile = Path(Path.cwd()/"Layout.csv")
csv_to_layout(ansKey,layoutFile)
    
    
