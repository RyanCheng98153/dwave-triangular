from src.solvers import Solver
from src.ising import Ising
from src.utils import getfileData
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
        solver: str = "None"
    ):
        sampleset = "nothing~"
        H, J = Ising.triangular(L, JL)
        self.Length = L
        solverType: PickSolver = PickSolver.NO_SOLVER
        
        if (solver == "exact" or solverType == PickSolver.EXACT_SOLVER):
            sampleset = Solver.doExactSolver(H, J)
            
        elif (solver == "qpu" or solverType == PickSolver.QPU_SOLVER):
            sampleset = Solver.doQPUSolver(H, J, f"triangular_L_{L}", 1)
        
        else:
            sampleset = "No Solver"
            raise ValueError( "Wanted a type of solver: not NO_SOLVER" )
        
        # print("=== Result ===")
        print(sampleset)
        Solver.printIsing(H, J)
        # return sampleset
        
    def runSpaceFile(self, filename:str, solver: str = "None"):
        file = getfileData( filename )
        H, J = Ising.spacefileConnect(file)
        if solver == "exact":
            sampleset = Solver.doExactSolver(H, J)
        elif solver == "qpu":
            sampleset = Solver.doQPUSolver(H, J, "test", 1)
        else:
            sampleset = "No Solver"
        
        # print("=== Result ===")
        # print(sampleset)
        Solver.printIsing(H, J)
        # return sampleset
        
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