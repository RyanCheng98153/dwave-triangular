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

def uniquifyFile(path:str)->str:
        filename, extension = os.path.splitext(path)
        counter = 1
        while os.path.exists(path):
            originPath = path
            path = filename + "(" + str(counter) + ")" + extension
            counter += 1
        if counter != 1:
            print(f"{originPath} has existed. --> {path} is now created.")
            pass
        return path
    
def displayAllSampleset(sampleset, num_vars:int):
    # make sampleset can show all results
    w = (log(num_vars) // log(10) +2)
    formatwidth = int(w * num_vars + 25)
    
    if formatwidth < 60:
        formatwidth = 60
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
