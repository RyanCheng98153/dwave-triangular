from src.solvers import Solver
from src.ising import Ising
from src.utils import getfileData, uniquifyFilename, formatSampleset
import sys, os
import fire

from enum import Enum
class PickSolver(Enum):
    NO_SOLVER:str = "Mone"
    EXACT_SOLVER:str = "exact"
    QPU_SOLVER:str = "qpu"

class Run(object):
    def __init__( self ):
        pass
    
    @staticmethod
    def runIsing(
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
        
        # beautiful format sampleset
        filestr = "=== Result ===\n" 
        formatted_sampleset = formatSampleset(sampleset, L*L)
        filestr += str(formatted_sampleset) + '\n'
        
        # choose the target directory and file 
        targetpath = f"./results/triangular/{solver.upper()}/"
        filename = f"tri_L{L}_JL_{JL}_{solver.upper()}_sam{numResult}_.txt"
        targetfile = uniquifyFilename(targetpath + filename)
        
        if not os.path.exists(targetpath):
            os.makedirs(targetpath)
        with open(targetfile, "w") as f:
            f.writelines(filestr)
        
        return sampleset
    
    @staticmethod
    def runSpaceFile(filename:str, solver: str = "None"):
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
        # Solver.printIsing(H, J, printMode=True)
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