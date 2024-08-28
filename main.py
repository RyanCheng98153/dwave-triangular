import sys
from src.graph import *
from src.solvers import Solver
from src.helper import Helper
import fire

from enum import IntEnum
class PickSolver(IntEnum):
    NO_SOLVER: int = 0
    EXACT_SOLVER: int = 1
    QPU_SOLVER:int = 2

class Run(object):
    def __init__( self ):
        pass
        
    def runIsing(self, 
        length:int = 3, 
        height:int = 1,
        JL:float = 1.0, 
        JH:float = 1.0, 
        solverType: PickSolver = PickSolver.NO_SOLVER,
    ):
        H, J = Solver.fullyConnect(length, height , JL, JH)
        self.Length, self.Height = length, height
        
        if (solverType == PickSolver.NO_SOLVER):
            raise ValueError( "Wanted a type of solver: not NO_SOLVER" )
            
        if (solverType == PickSolver.EXACT_SOLVER):
            solver = Solver(self.Length, self.Height)
            sampleset = solver.doExactSolver(H, J)
            # print("=== Result ===")
            # print(sampleset)
            # solver.printIsing(_H, _J)
            
            return sampleset
        if (solverType == PickSolver.QPU_SOLVER):
            solver = Solver(self.Length, self.Height)
            sampleset = solver.doQPUSolver(H, J)
            # print("=== Result ===")
            # print(sampleset)
            # solver.printIsing(_H, _J)
            
            return sampleset
        else:
            return
        
    def runSpaceFile(self, filename:str):
        file = Helper.getfileData( filename )
        self.Length, self.Height = Helper.getModelSize(file)
        H, J = Solver.spacefileConnect(file)
        
        self.__runExactSolver(H, J)

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