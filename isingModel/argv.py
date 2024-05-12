import argparse

class Args:
    def __init__(self, 
                 _L: int = 3,  
                 _H: int = None,
                 _JLayer: float = 1.0, 
                 _JHeight: float = 1.0, 
                ) -> None:
        
        self.L:int = _L
        self.H:int = _H
        self.JLayer:float = _JLayer
        self.JHeight:float = _JHeight
        
    def getLength( self ) -> int:
        return self.L
    
    def getHeight( self ) -> int:
        return self.H
    
    def getJLayer( self ) -> int:
        return self.JLayer
    
    def getJHeight( self ) -> int:
        return self.JHeight
    
        
    def inArgs():
        parser = argparse.ArgumentParser()
        parser.add_argument("J")
        args = parser.parse_args()
        
        return args