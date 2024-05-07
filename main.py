import sys
import argparse
# from argv import Args
from graph import *
import utils
from solvers import Solver

def main( Length:int, Height:int ):
    H = dict()
    J = dict()
    
    JLayer = 1.0
    JHeight = 1.0
    
    for i in range(0, L):
        for j in range(0, L):
            # x, y = toCoordinate()
            index = toIndex(Length, i, j)
            H[index] = 0
    
    for i in range(0, L):
        for j in range(0, L):
            # x, y = toCoordinate()
            index = toIndex(Length, i, j )
            right = getRight(Length, index )
            bottom = getBottom(Length, index)
            bottomRight = getBottomRight(Length, index )
            
            J[(index, right)] = 1
            J[(index, bottom)] = 1
            J[(index, bottomRight)] = 1
            
    solver = Solver(Length, Height, JLayer, JHeight)
    solver.doExactSolver(H, J)
    solver.printIsing(None, J)


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
        