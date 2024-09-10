import dimod
from dwave.system import DWaveSampler, EmbeddingComposite
from src.utils import toIndex, getRight, getBottom, getBottomRight

class Solver:
    @staticmethod
    def doExactSolver(_H: dict, _J: dict):
        sampler: dimod.ExactSolver = dimod.ExactSolver()
        sampleset = sampler.sample_ising(_H, _J)
        
        return sampleset
        
    @staticmethod
    def doQPUSolver(_H, _J, _taskname, _num_samples: int):
        sampler: EmbeddingComposite = EmbeddingComposite(DWaveSampler())
        sampleset = sampler.sample_ising( _H, _J, label=_taskname, num_reads=_num_samples)
        
        return sampleset
    
    @staticmethod
    def printIsing(_H, _J):
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
                    