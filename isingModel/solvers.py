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
    
    def spacefileConnect(file:str) -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        index = 1
        for i in range ( len(file) ):
            if("config" in file[i]):
                index = i
                break
        
        for i in range ( index, len(file) ):
            config = file[i].split()
            if( len(config) == 2 ):
                node = int( config[0] )
                magnetic_field = float( config[1] )
                H[node] = magnetic_field
                
            if( len(config) == 3 ):
                node1 = int( config[0] )
                node2 = int( config[1] )
                strength = float( config[2] )
                J[(node1, node2)] = strength
                
        
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
            
        print("\n == Jconnected == ")
        
        Jkeys = list(J.keys())
        key1 = None
        key2 = []
        val = []
        
        for k in Jkeys:
            if( key1 != k[0] ):
                if(key1 != None):
                    # print(f"[{key1}] -> {key2}: {val}")
                    print(f"[{key1}] -> {key2}: {[ f"{key2[i]}: {val[i]}" for i in range(0, len(key2)) ]}")
                    
                key1 = k[0]
                key2 = []
                val = []
            key2.append(k[1])
            val.append(J[k])
        
        # print(f"[{key1}] -> {key2}: {val}")
        print(f"[{key1}] -> {key2}: {[ str(key2[i]) + ': ' + str(val[i]) for i in range(0, len(key2)) ]}")
        