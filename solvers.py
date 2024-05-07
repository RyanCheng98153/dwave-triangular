from dimod import BinaryQuadraticModel
import dimod

class Solver:
    def __init__(self, _L, _H, _JL, _JH) -> None:
        bqm = BinaryQuadraticModel('BINARY')
        self.length = _L
        self.height = _H
        self.JLayer = _JL
        self.JHeight = _JH
        pass
    
    def doExactSolver(self, H, J):
        sampleset = dimod.ExactSolver().sample_ising(H, J)
        
        print("=== Result ===")
        print(sampleset)
    
    def printIsing(self, H, J, Graph = False):
        print("\n == Jconnected == ")
        
        if( H!=None ):
            for i in range(0, L):
                print(f"[ {i} ]: {H[i]}")
        
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
        