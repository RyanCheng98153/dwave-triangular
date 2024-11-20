from enum import Enum
from typing import List
from copy import deepcopy
from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx


class Spin(Enum):
    UP = 1
    DOWN = 0

class NodeType(Enum):
    Green = 0
    Red = 1
    Blue = 2
    Center = 3

class BondType(Enum):
    Triangle = 0
    Hexagon = 1
    Dimer = 2
    
class Node:
    def __init__(self, _id:int):
        self.id         :int = _id
        self.clean_id   :int = _id
        self.spin:Spin = Spin.UP
        
        self.NodeType   :NodeType = None
        
        self.right      :Node = None
        self.bottom     :Node = None
        self.bottomRight:Node = None
        
        self.JRight      :float = 0.0
        self.JBottom     :float = 0.0
        self.JBottomRight:float = 0.0
        
        self.rightType         :BondType = None
        self.bottomType        :BondType = None
        self.bottomRightType   :BondType = None

class NodeHelper:
    def __init__(self, _L:int, _W:int):
        self.L:int = _L
        self.W:int = _W
    
    def getCood(self, _id):
        return _id // self.W, _id % self.W
    
    def getId(self, _i, _j):
        return _i * self.W + _j
    
    def getRight(self, _id):
        i, j = self.getCood(_id)
        return self.getId( i, (j+1) % self.W ) 
    
    def getBottom(self, _id):
        i, j = self.getCood(_id)
        return self.getId( (i+1) % self.L, j )
    
    def getBottomRight(self, _id):
        i, j = self.getCood(_id)
        return self.getId( (i+1) % self.L, (j+1) % self.W )

    # reversed position
    def getRight(self, _id):
        i, j = self.getCood(_id)
        return self.getId( i, (j+1) % self.W ) 
    
    def getBottom(self, _id):
        i, j = self.getCood(_id)
        return self.getId( (i+1) % self.L, j )
    
    def getBottomRight(self, _id):
        i, j = self.getCood(_id)
        return self.getId( (i+1) % self.L, (j+1) % self.W )

class KagomeGraph:
    def __init__(self, _L:int, _W:int, _hexInit:int):
        self.L = _L
        self.W = _W
        self.nodes      :List[Node] = [Node(i) for i in range(0, _L*_W)]
        # self.hexInit    :int = _hexInit
        self.helper     :NodeHelper = NodeHelper(_L, _W)
    
    def getIdentify(self, _id):
        '''
        if identify of id is 0, identify as green node
        if identify of id is 1, identify as red node
        if identify of id is 2, identify as blue node
        if identify of id is 3, identify as hexagon center hole
        '''
        i, j = self.helper.getCood(_id)
        return 2 * (i%2) + (j%2)
    
    def makeGraph(self):
        for i in range(0, self.L):
            for j in range(0, self.W):
                srcId = self.helper.getId(i, j)
                # Hexagon center hole
                if self.getIdentify(srcId) == 3:
                    self.nodes[srcId] = None
                    continue
                self.nodes[srcId].right = self.nodes[self.helper.getRight(srcId)]
                self.nodes[srcId].bottom = self.nodes[self.helper.getBottom(srcId)]
                self.nodes[srcId].bottomRight = self.nodes[self.helper.getBottomRight(srcId)]
                
                # Green
                if self.getIdentify(srcId) == 0:
                    self.nodes[srcId].NodeType = NodeType.Green
                    self.nodes[srcId].bottomRight = None
                    continue
                # Red 
                if self.getIdentify(srcId) == 1:
                    self.nodes[srcId].NodeType = NodeType.Red
                    self.nodes[srcId].bottom = None
                    continue
                # Blue
                if self.getIdentify(srcId) == 2:
                    self.nodes[srcId].NodeType = NodeType.Blue
                    self.nodes[srcId].right = None
                    continue
                    
    def bondGraph(self, _JTriangle:float, _JHexagon: float, _JDimer: float):
        for i in range(0, self.L):
            for j in range(0, self.W):
                srcId = self.helper.getId(i, j)
                # is hexagon hole
                if self.nodes[srcId] == None:
                    # empty(None) Node don't have member variable of right, bottom, bottomRight
                    # so, find right, bottom, bottomRight from graph
                    continue
                    
                # is a regular node
                srcNode = self.nodes[srcId]
                
                if srcNode.NodeType == NodeType.Green:
                    srcNode.JRight = _JHexagon
                    srcNode.JBottom = _JHexagon
                    continue
                if srcNode.NodeType == NodeType.Red:
                    srcNode.JRight = _JHexagon
                    srcNode.JBottomRight = _JHexagon
                    continue
                if srcNode.NodeType == NodeType.Blue:
                    srcNode.JBottom = _JHexagon
                    srcNode.JBottomRight = _JHexagon
                    continue
                
    def getAdjList(self):
        adjList = []
        for srcNode in self.nodes:
            if srcNode == None:
                continue
            for adjNode, bondStrength, bondType in [[srcNode.right, srcNode.JRight,srcNode.rightType], 
                                                [srcNode.bottom, srcNode.JBottom, srcNode.bottomType], 
                                                [srcNode.bottomRight, srcNode.JBottomRight, srcNode.bottomRightType]]:
                if adjNode == None:
                    continue
                adjList.append([srcNode.id, adjNode.id, bondStrength, bondType])
        
        return adjList
    
class Visualize:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def visualize( _graph: KagomeGraph, labelHexagon = False, showStrength=False ):
        G: nx.Graph = nx.empty_graph( n=0 )
        
        def getPosition (_id):
            y, x = _id // _graph.W, _id % _graph.W
            y = _graph.L-1-y
            return (x, y)
        def getLightColor (color):
            if color == "Red" or color == "red":
                return "pink"
            return "light" + color
        
        def getSpinColor(spin: Spin):
            if spin == Spin.UP:
                return "lightblue"
            if spin == Spin.DOWN:
                return "blue"
        
        # add MLGraphs nodes to networkx graph
        if labelHexagon:
            G.add_nodes_from( getPosition( id ) for id in range(len(_graph.nodes)) )
            color_map = [getSpinColor(node.spin)  if node is not None else "grey" for node in _graph.nodes]
            # color_map = [(node.NodeType.name)  if node is not None else "grey" for node in _graph.nodes]
            
        else:
            # ignore the hexagon None ndoes
            G.add_nodes_from( getPosition(node.id) for node in _graph.nodes if node is not None )
            color_map = [getSpinColor(node.spin) for node in _graph.nodes if node is not None]
            # color_map = [(node.NodeType.name) for node in _graph.nodes if node is not None]

        nodelist = deepcopy(G.nodes()) # using deep copy not shallow copy because nx.network may return reference
        
        def getBondStyle(bondType: BondType) -> tuple[str, str]:
            if bondType == BondType.Hexagon:
                return "blue", "-"
            if bondType == BondType.Triangle:
                # return "orange", ":"
                return "orange", "--"
            if bondType == BondType.Dimer:
                return "red", "-"
            
        for srcId, adjId, bondStrength, bondType in _graph.getAdjList():
            if bondType == None:
                bondColor, bondStyle = "black", "-"
            else:
                bondColor, bondStyle = getBondStyle(bondType)
                
            srcX, srcY = getPosition(srcId)
            
            # right bottom periodic
            if srcId == len(_graph.nodes) -1 and adjId == 0:
                G.add_edge( (srcX, srcY) , (_graph.W, -1), weight=bondStrength, bondColor=bondColor, bondStyle=bondStyle)
                
                # add color of the right bottom periodic 
                color_map.append( getLightColor(_graph.nodes[adjId].NodeType.name) )
                continue
            # right periodic column
            if (srcId+1) % _graph.W == 0 and adjId % _graph.W == 0:
                adjX, adjY = getPosition(adjId)
                G.add_edge( (srcX, srcY), (_graph.W, adjY), weight=bondStrength, bondColor=bondColor, bondStyle=bondStyle)
                
                # add color of the right periodic 
                color_map.append( getLightColor(_graph.nodes[adjId].NodeType.name) )
                continue
            # bottom periodic row
            if srcId // _graph.W == _graph.L-1 and adjId // _graph.W == 0:
                adjX, adjY = getPosition(adjId)
                G.add_edge( (srcX, srcY), (adjX, -1), weight=bondStrength, bondColor=bondColor, bondStyle=bondStyle)
                
                # add color of the bottom periodic
                color_map.append( getLightColor(_graph.nodes[adjId].NodeType.name) )
                continue
            G.add_edge( (srcX, srcY), getPosition(adjId), weight=bondStrength, bondColor=bondColor, bondStyle=bondStyle)
        
        pos = dict( ((i, j), (i+j/2, j*sqrt(3))) for (i, j) in G.nodes() ) #Dictionary of all positions
        labels = dict( ((i, j), index) for index, (i, j) in enumerate(nodelist) ) #Add the labels to the nodes
        
        # draw
        bondColor = nx.get_edge_attributes(G, 'bondColor').values()
        bondStyle = nx.get_edge_attributes(G, 'bondStyle').values()
        # nodeColor = nx.get_edge_attributes(G, "nodeColor").values()
        weight_labels = nx.get_edge_attributes(G,'weight')
        
        node_width = 250 if _graph.L == 7 else 200
        edge_width = 3 if _graph.L == 7 else 2
        font_size = 10 if _graph.L == 7 else 8
        
        # constrast font color with node color
        def getConstrastColor(color):
            if color == "black":
                return "white"
            if color == "white":
                return "black"
            return color
        
        # fontcolor_map = [getConstrastColor(color) for color in color_map]
        # fontcolor_map = [getConstrastColor(color) for color in color_map]
        

        
        nx.draw(G, pos, labels=labels, with_labels=True, 
                node_size=node_width, font_size=font_size, font_color = "black",
                node_color = color_map, edgecolors="black",
                edge_color=bondColor, width=edge_width, style=bondStyle)    
        # add label of bond edge strength
        if showStrength:
            nx.draw_networkx_edge_labels(G,pos,edge_labels=weight_labels)
        
        plt.show()