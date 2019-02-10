from configs import *

def readCsv(fileName):
    f = open(filePath + fileName, "r")
    return f.read()