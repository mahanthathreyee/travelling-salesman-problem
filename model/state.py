class State:
    cost: float = 0
    tour_cost: float = 0

    current_city_id: int = None
    path: list[int] = []
    
    unvisited: set[int] = set()

    _n_cities = 0

    def __init__(self, source_id: int, n_cities: int, branch_state: bool=False) -> None:
        self.current_city_id = source_id
        self._n_cities = n_cities
        
        if not branch_state:
            self.path += [ source_id ]
            self.unvisited = set( range(n_cities) ) - { source_id }

    def __lt__(self, other):
        return self.cost < other.cost
    
    def __le__(self, other):
        return self.cost <= other.cost
    
    def construct_new_state(self, neighbor_id: int, cost: float, tour_cost: float) -> 'State':
        new_state = State(
            source_id=neighbor_id, 
            n_cities=self._n_cities, 
            branch_state=True
        )

        new_state.cost = cost
        new_state.tour_cost = self.tour_cost + tour_cost
        new_state.path = self.path + [ neighbor_id ]
        new_state.unvisited = self.unvisited - { neighbor_id }

        return new_state

    def __repr__(self):
        import json

        readable_data = {
            'current_city_id': self.current_city_id,
            'cost': self.cost,
            'path': self.path,

            '__classname__': str(self.__class__.__name__)
        }
        
        return json.dumps(readable_data)