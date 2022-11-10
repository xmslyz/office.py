from abc import ABC, abstractmethod


class Record(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_new(self):
        pass

