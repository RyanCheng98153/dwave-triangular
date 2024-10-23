from src.utils import toIndex, getRight, getBottom, getBottomRight, timer_func

class Ising:
    @staticmethod
    def triangular( _L:int, _JLayer: float) -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        for i in range(0, _L):
            for j in range(0, _L):
                # x, y = toCoordinate()
                index = toIndex(_L, i, j )
                right = getRight(_L, index )
                bottom = getBottom(_L,  index)
                bottomRight = getBottomRight(_L, index )
                
                J[(index, right)] = _JLayer
                J[(index, bottom)] = _JLayer
                J[(index, bottomRight)] = _JLayer
        
        return H, J
    
    # @timer_func
    @staticmethod
    def spacefileConnect(file:list[str]) -> tuple[dict, dict]:
        H = dict()
        J = dict()
        
        for i in range (len(file)):
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
    