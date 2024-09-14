from math import log
from dimod.serialization.format import Formatter
import os.path

def getfileData(filestr:str):
    with open(filestr) as f:
        data = [line for line in f.readlines() if not line.startswith("#")]
        return data

def getAPItoken(filepath:str):
    with open(filepath, 'r', encoding='utf-8') as F:
        return F.readlines()

def uniquifyFilename(path:str)->str:
        filename, extension = os.path.splitext(path)
        counter = 1
        while os.path.exists(path):
            originPath = path
            path = filename + "(" + str(counter) + ")" + extension
            counter += 1
        if counter != 1:
            pass
            # print(f"{originPath} has existed. --> {path} is now created.")
        return path
    
def formatSampleset(sampleset, var_num:int):
    w = (log(var_num) // log(10) +2)
    formatwidth = int(w * var_num + 25)
    
    formatted_sampleset = Formatter(width = formatwidth).format(sampleset)
    return formatted_sampleset

def toIndex(L, _i, _j) -> int:
    return L*_i + _j

def toTuple(L, _index):
    i = _index // L
    j = _index % L
    return i, j

def getRight(L, _index) -> int:
    i, j = toTuple( L, _index)
    j = (j+1) % L
    return L*i + j

def getBottom(L, _index):
    i, j = toTuple( L, _index)
    i = (i+1) % L
    return L*i + j

def getBottomRight(L, _index):
    i, j = toTuple( L, _index)
    i = ( i+1 ) % L
    j = ( j+1 ) % L
    return L*i + j
