from dimod import BinaryQuadraticModel
from isingModel.utils import *
import dimod

class Solver:
    def __init__(self, _L, _H) -> None:
        bqm = BinaryQuadraticModel('BINARY')
        self.length = _L
        self.height = _H
        
        pass
    
    def fullyConnect( self, J_layer, J_height=1.0 ) -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        for i in range(0, self.length):
            for j in range(0, self.length):
                # x, y = toCoordinate()
                index = toIndex(self.length, i, j)
                H[index] = 0
        
        for i in range(0, self.length):
            for j in range(0, self.length):
                # x, y = toCoordinate()
                index = toIndex(self.length, i, j )
                right = getRight(self.length, index )
                bottom = getBottom(self.length,  index)
                bottomRight = getBottomRight(self.length, index )
                
                J[(index, right)] = J_layer
                J[(index, bottom)] = J_layer
                J[(index, bottomRight)] = J_layer
        
        return H, J
    
    def customConnect() -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        return H, J
    
    def doExactSolver(self, H, J):
        sampleset = dimod.ExactSolver().sample_ising(H, J)
        
        print("=== Result ===")
        print(sampleset)
    
    def printIsing(self, H, J, Graph = False):
        print("\n == Magnetic Field == ")
        
        if( H!=None ):
            Hkeys = list(H.keys())
            for k in Hkeys:
                print(f"[{k}]: {H[k]}")
                
        Jkeys = list(J.keys())
        key1 = None
        key2 = []
        
        for k in Jkeys:
            if( key1 != k[0] ):
                if(key1 != None):
                    print(f"[{key1}]: {key2}")
                
                key1 = k[0]
                key2 = []
            key2.append(k[1])
        
        print(f"[{key1}]: {key2}")
        