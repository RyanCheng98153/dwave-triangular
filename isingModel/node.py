from enum import Enum

class Spin(Enum):
    Up = 1
    Down = -1

class Node:
    def __init__( self, 
                 _id = None,
                 _spin = Spin.Up, 
                 ) -> None:
        
        self.id = _id
        self.spin:   Spin = _spin
        
        # index of neighborNodes
        self.rightNode: Node =  None
        self.bottomNode: Node = None
        self.bottomRightNode: Node = None
        
        # bonds strength of each nodes
        self.J_right: float = 0.0
        self.J_bottom: float = 0.0
        self.J_bottomRight: float = 0.0
        
    def setId(self, _id):
        self.id = _id
    
    def setSpin(self, _s:Spin):
        self.spin = _s
        
    def flipSpin(self):
        self.spin = Spin.Up if self.spin == Spin.Down else Spin.Down
        
    def bondRight(self, _node, _bondJ):
        self.rightNode = _node
        self.J_right = _bondJ
        
    def bondBottom(self, _node, _bondJ):
        self.bottomNode = _node
        self.J_bottom = _bondJ
     
    def bondBottomRight(self, _node, _bondJ):
        self.bottomRightNode = _node
        self.J_bottomRight = _bondJ
        
