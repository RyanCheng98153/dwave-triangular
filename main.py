import sys
# from argv import Args
from isingModel.graph import *
from isingModel.solvers import Solver
import json
import os

def getfileData(filestr:str):
    with open(filestr) as f:
        data = f.readlines()
        return data

def getJson(filestr:str):
    return json.loads( getfileData(filestr) )

def getModelSize(file:str):
    for i in range ( len(file) ):
        if("model_size" in file[i]):
            model_size = file[i+1].split()
            return int(model_size[0]), int(model_size[2])

def main():
    H = dict()
    J = dict()
    
    inputStr = sys.argv[1]
    
    Length = 1.0
    Height = 1.0
    
    if (inputStr.isnumeric()):
        Length = int( inputStr )
    
    if (os.path.exists(inputStr)):    
        file = getfileData( inputStr )
        Length, Height = getModelSize(file)
    else:
        print("exit: invalid str!")
        exit()
    
    file = getfileData( inputStr )
    H, J = Solver.spacefileConnect(file)
    
    solver = Solver(Length, Height)
    solver.doExactSolver(H, J)
    solver.printIsing(H, J)

def test(status:bool):
    # for testing
    if( status == False):
        return
    else:
        # input = int(sys.argv[1])
        exit()

    
if __name__ == "__main__":
    test(False)
    
    if (len(sys.argv) == 1):
        print("exit: Please insert input!")
        exit()
        
    main()