from __future__ import annotations

#region Type Checking
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.edge import Edge
#endregion

class Node:
    id: int = 0
    neighbors: list[Edge] = []

    def __init__(self, id: int) -> None:
        self.id = id

    def __repr__(self):
        import json

        readable_data = {
            'id': self.id,
            'neighbors': [neighbor.__repr__() for neighbor in self.neighbors],

            '__classname__': str(self.__class__.__name__)
        }
        
        return json.dumps(readable_data)
