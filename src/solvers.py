import dimod
from dwave.system import DWaveSampler, EmbeddingComposite, LeapHybridSampler
from src.utils import timer_func

class Solver:
    # @timer_func
    @staticmethod
    def doExactSolver(_H: dict, _J: dict):
        sampler: dimod.ExactSolver = dimod.ExactSolver()
        sampleset = sampler.sample_ising(_H, _J)
        
        return sampleset
    
    # @timer_func
    @staticmethod
    def doQPUSolver(_H, _J, _taskname, _num_samples: int):
        sampler: EmbeddingComposite = EmbeddingComposite(DWaveSampler())
        sampleset = sampler.sample_ising( _H, _J, label=_taskname, num_reads=_num_samples)
        
        return sampleset
    
    # @timer_func
    @staticmethod
    def doHybridSolver(_H, _J, _taskname):
        sampler: LeapHybridSampler = LeapHybridSampler()
        sampleset = sampler.sample_ising( _H, _J, label=_taskname)
        
        return sampleset
    
    
    @staticmethod
    def printIsing(_H, _J, printMode=True):
        printString = ""
        if( len(_H) != 0 ):
            print("\n == Magnetic Field == ")
            Hkeys = list(_H.keys())
            for k in Hkeys:
                printString += (f"[{k}]: {_H[k]}") + '\n'
                
        printString += ("\n == Jconnected == ") + '\n'
        
        Jkeys = list(_J.keys())
        key1 = None
        key2 = []
        val = []
    
        for k in Jkeys:
            if( key1 != k[0] ):
                if(key1 != None):
                    printString += (f"[{key1}] -> {key2}: {val}") + '\n'
                key1 = k[0]
                key2 = []
                val = []
            key2.append(k[1])
            val.append( _J[(k[0], k[1])])
        printString += (f"[{key1}] -> {key2}: {val}") + '\n'
        
        if printMode:
            print(printString)
        else:
            return printString