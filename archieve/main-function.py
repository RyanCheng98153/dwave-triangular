import os, sys
from src.solvers import Solver
from src.helper import Helper


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
        file = Helper.getfileData( inputStr )
        Length, Height = Helper.getModelSize(file)
        H, J = Solver.spacefileConnect(file)
        
    else:
        print("exit: invalid str!")
        exit()
    
    solver = Solver(Length, Height)
    # solver.doExactSolver(_H, _J)
    solver.doQPUSolver(H, J)
    # solver.printIsing(H, J)
    