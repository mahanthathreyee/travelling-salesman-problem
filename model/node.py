from edge import Edge
from collections import defaultdict

class Node:
    id: int = 0
    name: str = ''
    neighbors: dict[Edge] = defaultdict(lambda: None)
