from dataclasses import dataclass


@dataclass
class Range:
    start: int
    stop: int

    @property
    def length(self):
        return (self.stop - self.start + 1)

    def __repr__(self):
        return f'[{self.start} - {self.stop} ({self.length})]'
