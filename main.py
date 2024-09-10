from src.helper import Helper
from src.solvers import Solver
# from src.graph import *
import sys
import fire

from enum import Enum
class PickSolver(Enum):
    NO_SOLVER: int = 0
    EXACT_SOLVER: int = 1
    QPU_SOLVER:int = 2

class Run(object):
    def __init__( self ):
        pass
        
    def runIsing(self, 
        L:int = 3,
        JL:float = 1.0, 
        # solverType: PickSolver = PickSolver.NO_SOLVER
    ):
        sampleset = "nothing~"
        H, J = Solver.fullyConnect(L, JL)
        self.Length = L
        solverType: PickSolver = PickSolver.EXACT_SOLVER
        
        if (solverType == PickSolver.NO_SOLVER):
            sampleset = "No Solver"
            raise ValueError( "Wanted a type of solver: not NO_SOLVER" )
            
        if (solverType == PickSolver.EXACT_SOLVER):
            print("hi")
            solver = Solver(L, JL )
            sampleset = solver.doExactSolver(H, J)
            
        if (solverType == PickSolver.QPU_SOLVER):
            solver = Solver(self.Length, JL)
            sampleset = solver.doQPUSolver(H, J, "test", 1)
            
        
        # print("=== Result ===")
        print(sampleset)
        solver.printIsing(H, J)
        # return sampleset
        
    def runSpaceFile(self, filename:str):
        file = Helper.getfileData( filename )
        self.Length, self.Height = Helper.getModelSize(file)
        H, J = Solver.spacefileConnect(file)
        
        sampleset = Solver.spacefileConnect(H, J)
        print(sampleset)

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