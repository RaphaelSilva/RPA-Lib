from drivers import Sequence


class Task():

    _sequences: list[Sequence]

    def __init__(self, sequences=list[Sequence]):
        self._sequences = sequences

    def Add(self, sequence: Sequence):
        self._sequences.append(self)
        return self

    def run(self):
        for seq in self._sequences:
            s: Sequence = seq
            s.execute()
