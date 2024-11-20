import argparse
from enum import Enum
from visualResult.kagome import KagomeGraph, Visualize, Spin
from math import sqrt

class Model(Enum):
    Triangular = "triangular"
    MapleLeaf = "mapleleaf"
    Kagome = "kagome"
    
    def __str__(self):
        return self.value

def main(_model: Model):
    
    with open(args.filename, "r") as f:
        datas = f.readlines()
    
    ids = [int(id) for id in datas[0].split()[:-2]]
    
    results = []
    for data in datas[1:]:
        if data.startswith("['SPIN'"):
            break
        if not data[0].isdigit():
            continue
        
        items = data.split()
        qubos = [ -1 if var == "-1" else 1 for var in items[1:-2] ]
        energy = items[-2]
        
        if energy.startswith("-"):
            energy = -1 * float(energy[1:])
        else:
            energy = float(energy)
        
        results.append( { "qubos": qubos, "energy": energy })
    
    # i = int(input("Pick Result: "))
    i = 0
    
    if _model == Model.Kagome:
        qubos = results[i]["qubos"]
        
        L:int = int(sqrt( len(qubos) * 4 / 3 ))
        W:int = L
        
        graph = KagomeGraph(L, W, 0)
        graph.makeGraph()
        graph.bondGraph(1.0, 1.0, 1.0)
        
        clean_node = filter(lambda node: node!=None and node.clean_id in ids, graph.nodes)
        
        for node, qubo in zip(clean_node, qubos):
            if qubo == 1:
                node.spin = Spin.UP
            if qubo == -1:
                node.spin = Spin.DOWN
            # print(f"{node.clean_id}: {node.id}")
        
        Visualize.visualize(graph, labelHexagon=False, showStrength=False)

    
if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", 
                        "--model",
                        type=Model,
                        choices=list(Model),
                        required=True
                        )

    parser.add_argument("-f", 
                        "--filename",
                        type=str,
                        required=True
                        )

    args = parser.parse_args()
    
    main( _model=args.model )