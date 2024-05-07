import sys
import argparse
# from argv import Args
from graph import *
import utils
from solvers import Solver

def main( Length:int, Height:int=1, JLayer = 1.0, JHeight = 1.0 ):
    H = dict()
    J = dict()
    
    for i in range(0, L):
        for j in range(0, L):
            # x, y = toCoordinate()
            index = toIndex(Length, i, j)
            H[index] = 0
            
    def fullyconnect(J):
        for i in range(0, L):
            for j in range(0, L):
                # x, y = toCoordinate()
                index = toIndex(Length, i, j )
                right = getRight(Length, index )
                bottom = getBottom(Length, index)
                bottomRight = getBottomRight(Length, index )
                
                J[(index, right)] = JLayer
                J[(index, bottom)] = JLayer
                J[(index, bottomRight)] = JLayer
        return J
    
    # J = fullyconnect(J)
    J = customBond(J)
            
    solver = Solver(Length, Height, JLayer, JHeight)
    solver.doExactSolver(H, J)
    solver.printIsing(None, J)

def customBond( J:dict ):
    print("insert the bonds")
    
    
    return J

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
        print("Please insert input!")
        exit()
    
    L = int(sys.argv[1])
        
    if(L % 3 == 0 and L>=3 ): 
        # args()
        main(L, 1)
    else:
        print("exit: invalid input")
        