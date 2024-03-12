from util.timer import Timer
from algorithms.algorithm_base import AlgorithmBase

class AlgorithmRunner:
    algorithm: AlgorithmBase
    timer: Timer

    def __init__(self, algorithm: AlgorithmBase) -> None:
        self.algorithm = algorithm
        self.timer = Timer()

    def run(self):
        self.timer.start()
        self.algorithm.execute()
        self.timer.end()

    def results(self):
        return {
            'Algorithm': self.algorithm.getName(),
            'Tour': self.algorithm.getTour(),
            'Cost': self.algorithm.getCost(),
            'Elapsed Time (ms)': self.timer.elapsed(),
            'Metadata': self.algorithm.getMetadata()
        }
