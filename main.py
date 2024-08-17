import sys
from src.graph import *
from src.solvers import Solver
from src.helper import Helper
import fire

class Run(object):
    def __init__( self ):
        pass
        
    def runIsing(self, 
        length:int = 3, 
        height:int = 1,
        JL:int = 1.0, 
        JH:int = 1.0 
    ):
        H, J = Solver.fullyConnect(length, height , JL, JH)
        self.Length, self.Height = length, height
        
        # self.__runQPUSolver(H, J)
        self.__runExactSolver(H, J)

    def runSpaceFile(self, filename:str):
        file = Helper.getfileData( filename )
        self.Length, self.Height = Helper.getModelSize(file)
        H, J = Solver.spacefileConnect(file)
        
        self.__runExactSolver(H, J)
        
    def __runExactSolver(self, _H, _J):
        solver = Solver(self.Length, self.Height)
        sampleset = solver.doExactSolver(_H, _J)
        print("=== Result ===")
        print(sampleset)
        solver.printIsing(_H, _J)
        
    def __runQPUSolver(self, _H, _J,):
        solver = Solver(self.Length, self.Height)
        sampleset = solver.doQPUSolver(_H, _J)
        print("=== Result ===")
        print(sampleset)
        solver.printIsing(_H, _J)

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