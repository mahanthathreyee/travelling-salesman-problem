from pathlib import Path

class Parameter:
    input_file: Path = None

    algorithm: str = None
    source_id: str = None

    heuristic: str = None

    initial_tour: str = None
    neighbor_tour: str = None
    alpha: float = None
    initial_threshold: float = None
    final_threshold: float = None

    def __repr__(self):
        import json

        readable_data = {
            'input_file': self.input_file,
            
            'algorithm': self.algorithm,
            'source_id': self.source_id,
            
            'heuristic': self.heuristic,

            'alpha': self.alpha,
            'initial_tour': self.initial_tour,
            'neighbor_tour': self.neighbor_tour,
            'initial_threshold': self.initial_threshold,
            'final_threshold': self.final_threshold,

            '__classname__': str(self.__class__.__name__)
        }
        
        return json.dumps(readable_data)
