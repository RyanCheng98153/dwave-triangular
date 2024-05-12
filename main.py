import sys
# from argv import Args
from isingModel.graph import *
from isingModel.solvers import Solver
import json

def getJson(file:str):
    #with open("9_9_1_gamma0_2.json") as f:
    with open(file) as f:
        data = f.readlines()
        return json.loads(data)

# def main( Length:int, Height:int ):
def main():
    H = dict()
    J = dict()
    
    Length:int = int(sys.argv[1])
    Height:int = 1
    
    J_layer = 1.0
    J_height = 1.0
    solver = Solver(Length, Height)
    H, J = solver.fullyConnect( J_layer, J_height)
    
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