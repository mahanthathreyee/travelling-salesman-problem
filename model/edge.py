from node import Node

class Edge:
    weight: int = 0
    
    source_id: int = 0
    source_node: Node = None

    destination_id: int = 0
    destination_node: Node = None

    bidirection = True

    def __init__(self, weight: int, source: Node, destination: Node) -> None:
        self.weight = weight
        
        self.source_id = source.id
        self.source_node = source
        
        self.destination_id = destination.id
        self.destination_node = destination