from pathlib import Path

class Parameter:
    input_file: Path = None

    algorithm: str = None

    heuristic: str = None
    source_id: str = None

    def __repr__(self):
        import json

        readable_data = {
            'input_file': self.input_file,
            'algorithm': self.algorithm,
            'heuristic': self.heuristic,
            'source_id': self.source_id,

            '__classname__': str(self.__class__.__name__)
        }
        
        return json.dumps(readable_data)
