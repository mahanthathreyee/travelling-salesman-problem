from __future__ import annotations

#region Type Checking
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.node import Node
#endregion
    
class Edge:
    weight: float = 0
    
    source_id: int = 0
    source_node: Node = None

    destination_id: int = 0
    destination_node: Node = None

    def __init__(self, weight: int, source: Node, destination: Node) -> None:
        self.weight = weight
        
        self.source_id = source.id
        self.source_node = source
        
        self.destination_id = destination.id
        self.destination_node = destination

    def __repr__(self):
        import json

        readable_data = {
            'weight': self.weight,
            'source_id': self.source_id,
            'destination_id': self.destination_id,
            'bidirection': self.bidirection,

            '__classname__': str(self.__class__.__name__)
        }

        return readable_data