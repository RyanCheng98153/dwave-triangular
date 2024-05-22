import sys
# from argv import Args
from isingModel.graph import *
from isingModel.solvers import Solver
import json
import os
import fire

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

class Run(object):
    def __init__( self ):
        pass
        
    def runIsing(self, 
        length:int = 3, 
        height:int = 1,
        JL:int = 1.0, 
        JH:int = 1.0 
    ):
        H, J = Solver.fullyConnect(length, height , JL, JH)
        self.Length, self.Height = length, height
        self.__runSolver(H, J)

    def runSpace(self, filename:str):
        print("Space!!")
        H, J = dict(), dict()
        file = getfileData( filename )
        self.Length, self.Height = getModelSize(file)
        H, J = Solver.spacefileConnect(file)
        
        self.__runSolver(H, J)
        
    def __runSolver(self, _H, _J):
        solver = Solver(self.Length, self.Height)
        solver.doExactSolver(_H, _J)
        solver.printIsing(_H, _J)

def main():
    H = dict()
    J = dict()
    
    inputStr = sys.argv[1]
    
    Length = 1
    Height = 1
    
    J_layer = 1.0
    J_height = 1.0
    
    if (inputStr.isnumeric()):
        Length = int( inputStr )
        print(Length)
        H, J = Solver.fullyConnect(Length, Height ,J_layer, J_height)
        
    elif (os.path.exists(inputStr)):    
        file = getfileData( inputStr )
        Length, Height = getModelSize(file)
        H, J = Solver.spacefileConnect(file)
        
    else:
        print("exit: invalid str!")
        exit()
    
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
    
    if (len(sys.argv) < 2):
        print("exit: Please insert input!")
        exit()
    
    fire.Fire(Run)