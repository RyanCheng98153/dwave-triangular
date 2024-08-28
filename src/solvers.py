from dimod import BinaryQuadraticModel
from src.utils import *
import dimod
from dwave.system import DWaveSampler, EmbeddingComposite


class Solver:
    def __init__(self, _L, _H) -> None:
        bqm = BinaryQuadraticModel('BINARY')
        self.length = _L
        self.height = _H
        
        pass
    
    def fullyConnect( _L:int, _H:int, J_layer:float, J_height:float=1.0 ) -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        for i in range(0, _L):
            for j in range(0, _L):
                # x, y = toCoordinate()
                index = toIndex(_L, i, j )
                right = getRight(_L, index )
                bottom = getBottom(_L,  index)
                bottomRight = getBottomRight(_L, index )
                
                J[(index, right)] = J_layer
                J[(index, bottom)] = J_layer
                J[(index, bottomRight)] = J_layer
        
        return H, J
    
    def spacefileConnect(file:str) -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        index = 1
        for i in range ( len(file) ):
            if("couplings" in file[i]):
                index = i
                break
        
        for i in range ( index, len(file) ):
            coupling = file[i].split()
            if( len(coupling) == 2 ):
                node = int( coupling[0] )
                magnetic_field = float( coupling[1] )
                H[node] = magnetic_field
            elif( len(coupling) == 3 ):
                node1 = int( coupling[0] )
                node2 = int( coupling[1] )
                strength = float( coupling[2] )
                J[(node1, node2)] = strength
                
        
        return H, J
    
    def doExactSolver(self, _H, _J):
        sampleset = dimod.ExactSolver().sample_ising(_H, _J,
                                                    label="Test Ising Problem 1",
                                                    num_reads=3)
        
        return sampleset
        
#    def doQPUSolver(self, _H, _J, _token:str):
    def doQPUSolver(self, _H, _J):
        # print(f"H: {_H}")
        # print(f"J: {_J}")
        sampler = EmbeddingComposite(DWaveSampler())

        sampleset = sampler.sample_ising( _H, _J,
                                 label="Test Ising Problem 1",
                                 num_reads=3)
        return sampleset
    
    def printIsing(self, _H, _J, Graph = False):
        if( len(_H) != 0 ):
            print("\n == Magnetic Field == ")
            Hkeys = list(_H.keys())
            for k in Hkeys:
                print(f"[{k}]: {_H[k]}")
                
        print("\n == Jconnected == ")
        
        Jkeys = list(_J.keys())
        key1 = None
        key2 = []
        val = []
    
        for k in Jkeys:
            if( key1 != k[0] ):
                if(key1 != None):
                    print(f"[{key1}] -> {key2}: {val}")
                    # print(f"[{key1}] -> {key2}: { [ f'{key2[i]}: {val[i]}' for i in range(0, len(key2)) ] } ")
                    
                key1 = k[0]
                key2 = []
                val = []
            key2.append(k[1])
            val.append( _J[(k[0], k[1])])
                    
        print(f"[{key1}] -> {key2}: {val}")
        # print(f"[{key1}] -> {key2}: { [ f'{key2[i]}: {val[i]}' for i in range(0, len(key2)) ] } ")
                    