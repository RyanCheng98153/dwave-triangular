from src.solvers import Solver
from src.ising import Ising
from src.utils import getfileData, uniquifyFilename
import sys, os
import fire

from enum import Enum
class PickSolver(Enum):
    NO_SOLVER: int = 0
    EXACT_SOLVER: int = 1
    QPU_SOLVER:int = 2

class Run(object):
    def __init__( self ):
        pass
    
    @staticmethod
    def runIsing(self, 
        L:int = 3,
        JL:float = 1.0, 
        solver: str = "None",
        numResult: int = 1
    ):
        sampleset = "nothing~"
        H, J = Ising.triangular(L, JL)
        solverType: PickSolver = PickSolver.NO_SOLVER
        
        if (solver == "exact" or solverType == PickSolver.EXACT_SOLVER):
            sampleset = Solver.doExactSolver(H, J)
            
        elif (solver == "qpu" or solverType == PickSolver.QPU_SOLVER):
            sampleset = Solver.doQPUSolver(H, J, f"tri_L_{L}_JL_{JL}", numResult)
        
        else:
            sampleset = "No Solver"
            raise ValueError( "Wanted a type of solver: not NO_SOLVER" )
        
        
        filestr = "=== Result ===\n" 
        filestr += str(sampleset) + '\n'
        
        targetpath = f"./results/triangular/{solver.upper()}/"
        filename = f"tri_L{L}_JL_{JL}_{solver.upper()}.txt"
        targetfile = uniquifyFilename(targetpath + filename)
        
        if not os.path.exists(targetpath):
            os.makedirs(targetpath)
        with open(targetfile, "w") as f:
            f.writelines(filestr)
        
        # return sampleset
    
    @staticmethod
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
        Solver.printIsing(H, J, printMode=True)
        return sampleset
        
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