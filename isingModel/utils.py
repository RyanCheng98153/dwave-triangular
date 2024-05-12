def toIndex(L, _i, _j) -> int:
    return L*_i + _j

def toTuple(L, _index):
    i = _index // L
    j = _index % L
    return i, j

def getRight(L, _index) -> int:
    i, j = toTuple( L, _index)
    j = (j+1) % L
    return L*i + j

def getBottom(L, _index):
    i, j = toTuple( L, _index)
    i = (i+1) % L
    return L*i + j

def getBottomRight(L, _index):
    i, j = toTuple( L, _index)
    i = ( i+1 ) % L
    j = ( j+1 ) % L
    return L*i + j
