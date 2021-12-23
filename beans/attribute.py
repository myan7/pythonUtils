# this is attribute.py, in which class attribute is designed.

class Attribute:
    def __init__(self, name, maxVal, minVal,length, dataType):
        self.name = name
        self.minVal = minVal
        self.maxVal = maxVal
        self.length = length
        self.dataType = dataType

    def __str__(self):
        _dict = {'name':self.name, 'maxVal': self.maxVal, 'minVal': self.minVal,'length': self.length, 'dataType': self.dataType}
        # print(f"name is {self.name}----\n{_dict}\n")
        return _dict
