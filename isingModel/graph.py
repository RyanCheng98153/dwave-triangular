from isingModel.utils import *
from isingModel.node import Node, Spin
        
class Graph:
    def __init__(self, 
                 _L = 3, 
                 _H = 1,
                 _JL = 1.0,
                 _JH = 1.0
                 ) -> None:
        if( _L % 3 != 0 and _L <= 0 ):
            return
        
        self.L = _L
        self.H = _H
        
        self.JLayer = _JL
        self.JHeight = _JH 
        
        self.nodeNums = self.L * self.L * self.H
        self.Graph:list[Node] = [ Node() ] * self.nodeNums
        self.makeGraph()
        
        
    #def __del__(self, name: str) -> None:
    #    pass
    
    def makeGraph(self):
        for i in range (0, self.L):
            for j in range (0, self.L):
                index = toIndex(i, j, self.L)
                self.Graph[index] = Node(index,  Spin.Down)
                self.Graph[index].bondRight          ( self.Graph[ getRight (index, self.L) ] , self.JLayer)
                self.Graph[index].bondBottom         ( self.Graph[ getBottom (index, self.L) ] , self.JLayer)
                self.Graph[index].bondBottomRight    ( self.Graph[ getBottomRight (index, self.L) ], self.JLayer)
        
    def printGraph(self):
        for i in range(0, self.L):
            for j in range(0, self.L):
                index = toIndex(i, j, self.L)
                print(f"{self.Graph[index].id}: {self.Graph[index].spin} right:{self.Graph[index].rightNode.id} bottom:{self.Graph[index].bottomNode.id} bottomRight:{self.Graph[index].bottomRightNode.id} ")


