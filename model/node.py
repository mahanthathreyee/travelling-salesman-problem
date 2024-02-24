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

    '''
    This function is needed to compare elements in priority queues. 
    It first compares the distances explored. If two cities have the
    same distance, their IDs are used as a tiebreaker. Since each 
    city has a unique ID, this ensures there are no ties.
    '''
    def __lt__(self, other):
        return self.id < other.id
    
    def __le__(self, other):
        return self.id <= other.id

    def __repr__(self):
        import json

        readable_data = {
            'id': self.id,
            'neighbors': [neighbor.__repr__() for neighbor in self.neighbors],

            '__classname__': str(self.__class__.__name__)
        }
        
        return json.dumps(readable_data)
