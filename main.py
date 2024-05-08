import sys
# from argv import Args
from graph import *
from solvers import Solver
import json

def getJson(file:str):
    #with open("9_9_1_gamma0_2.json") as f:
    with open(file) as f:
        data = str()
        for line in f.readlines():
            data += line
            
        return json.loads(data)
        
        # data = f.readlines()
        # return json.loads(data)
        
# def main( Length:int, Height:int ):
def main():
    H = dict()
    J = dict()
    
    jdata = getJson(sys.argv[1])
    
    
    model_info = jdata["model_info"]
    Length = model_info["length"]
    Height = model_info["height"]
    
    solver = Solver(Length, Height)
    
    for node in jdata["nodes"]:
        index = node["id"]
        magnetic_field = node["magnetic_field"]
        H[index] = magnetic_field
    
    for bond in jdata["bonds"]:
        srcNode = bond["node_ids"][0]
        tgtNode = bond["node_ids"][1]
        strength = bond["strength"]
        
        J[(srcNode, tgtNode)] = strength
    
    # print(H)
    # print(J)
    
    solver = Solver(Length, Height)
    solver.doExactSolver(H, J)
    solver.printIsing(H, J)


def test(status:bool):
    # for testing
    if( status == False):
        return
    else:
        # input = int(sys.argv[1])
        exit()

    
if __name__ == "__main__":
    test(False)
    
    if (len(sys.argv) == 1):
        print("exit: Please insert input!")
        exit()
    
    main()