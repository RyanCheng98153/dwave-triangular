from src.solvers import Solver
from src.ising import Ising
from src.utils import getfileData, uniquifyFile, displayAllSampleset
import sys, os
import fire

from enum import Enum
class PickSolver(Enum):
    NO_SOLVER:str = "none"
    EXACT_SOLVER:str = "exact"
    QPU_SOLVER:str = "qpu"
    HYBRID_SOLVER:str = "hybird"

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
            sampleset = Solver.doQPUSolver(H, J, f"qpu_tri_L_{L}_JL_{JL}_sam{numResult}", numResult)
        
        elif (solver == "hybrid" or solverType == PickSolver.HYBRID_SOLVER):
            """hybrid can only have 1 result"""
            sampleset = Solver.doHybridSolver(H, J, f"hybrid_tri_L_{L}_JL_{JL}_sam1")
        
        else:
            sampleset = "No Solver"
            raise ValueError( "Wanted a type of solver: not NO_SOLVER" )
        
        # beautiful format sampleset
        formatted_sampleset = displayAllSampleset(sampleset, L*L)
        filestr = str(formatted_sampleset) + '\n'
        
        # choose the target directory and file 
        dir = f"./results/triangular/{solver.upper()}/"
        output_filename = f"tri_L{L}_JL_{JL}_{solver.upper()}_sam{numResult}_.txt"
        targetfile = uniquifyFile(dir + output_filename)
        
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(targetfile, "w") as f:
            f.writelines(filestr)
        
        return sampleset
    
    @staticmethod
    def runSpaceFile(
        filename:str, 
        solver: str = "None",
        numResult: int = 1
        
    ):
        file = getfileData( filename )
        H, J = Ising.spacefileConnect(file)
        
        filename = filename.split("/")[-1].split('\\')[-1]
        if solver == "exact":
            sampleset = Solver.doExactSolver(H, J)
        
        elif solver == "qpu":
            sampleset = Solver.doQPUSolver(H, J, f"qpu_{filename}_sam{numResult}", numResult)
        
        elif (solver == "hybrid"):
            """hybrid can only have 1 result"""
            sampleset = Solver.doHybridSolver(H, J, f"hybrid_{filename}_sam1")
        
        else:
            sampleset = "No Solver"
        
        # beautiful format sampleset
        num_vars = len(sampleset.record[0][0])
        
        formatted_sampleset = displayAllSampleset(sampleset, num_vars)
        filestr = str(formatted_sampleset) + '\n'
        
        # choose the target directory and file 
        dir = f"./results/custom/{solver.upper()}/"
        
        fname, extension = os.path.splitext(filename)
        output_filename = f"{fname}_{solver.upper()}_sam{numResult}_.txt"
        targetfile = uniquifyFile(dir + output_filename)
        
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(targetfile, "w") as f:
            f.writelines(filestr)
        
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