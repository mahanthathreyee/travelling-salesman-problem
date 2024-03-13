import heapq

from model.edge import Edge
from model.node import Node

from heuristics.heuristic_base import HeuristicBase

class PrimsMST(HeuristicBase):
    NAME: str = 'Prims MST'

    def include_active_edges(self, edge_queue: list[Edge], source_id: int, unmarked_nodes: set[int], visited_nodes: set[int]):
        for neighbor_path in self.city_graph[source_id].neighbors:
            if neighbor_path.destination_id in unmarked_nodes and neighbor_path.destination_id not in visited_nodes:
                heapq.heappush(edge_queue, neighbor_path)

    def compute_cost(self, source_id: int, start_id: int, unmarked_nodes: set[int]) -> float:
        frozen_unmarked_nodes = frozenset(unmarked_nodes)
        if frozen_unmarked_nodes in self.cache:
            return self.cache[frozen_unmarked_nodes]

        edge_queue: list[Edge] = []

        null_node = Node(id=-1)
        initial_edge = Edge(
            weight=0,
            source=null_node,
            destination=self.city_graph[source_id]
        )
        heapq.heappush(edge_queue, initial_edge)

        heuristic_cost: float = 0
        visited_nodes: set[int] = set()

        while edge_queue:
            explore_edge = heapq.heappop(edge_queue)
            
            if explore_edge.destination_id in visited_nodes: 
                continue
            
            heuristic_cost += explore_edge.weight
            visited_nodes.add(explore_edge.destination_id)

            if len(visited_nodes) == self.n_cities:
                break

            self.include_active_edges(
                edge_queue=edge_queue,
                source_id=explore_edge.destination_id,
                unmarked_nodes=unmarked_nodes,
                visited_nodes=visited_nodes
            )

        start_to_nearest_unmarked = float('inf')
        for neighbor_path in self.city_graph[start_id].neighbors:
            if neighbor_path.destination_id in unmarked_nodes and neighbor_path.weight < start_to_nearest_unmarked:
                start_to_nearest_unmarked = neighbor_path.weight

        heuristic_cost += start_to_nearest_unmarked

        self.cache[frozen_unmarked_nodes] = heuristic_cost
        return heuristic_cost
