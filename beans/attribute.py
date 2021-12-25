# this is attribute.py, in which class attribute is designed.


# 20211223 log: need to add field of precision


class Attribute:
    def __init__(self, name, maxVal, minVal,length, dataType, precision=0):
        self.name = name
        self.minVal = minVal
        self.maxVal = maxVal
        self.length = length
        self.dataType = dataType
        self.precision = precision

    def __str__(self):
        _dict = {'name':self.name, 'maxVal': self.maxVal, 'minVal': self.minVal,'length': self.length, 'dataType': self.dataType,'precision':self.precision}
        return _dict
