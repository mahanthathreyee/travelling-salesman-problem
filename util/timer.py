from timeit import default_timer as BaseTimer

class Timer:
    start: float = None
    end: float = None

    def start(self):
        self.start = BaseTimer()

    def end(self):
        self.end = BaseTimer()

    def restart(self):
        self.end = None
        self.start()

    def elapsed(self) -> float:
        return (self.end - self.start) * 1000
