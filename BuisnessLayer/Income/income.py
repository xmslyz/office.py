from abc import ABC, abstractmethod


class Income(ABC):

    @abstractmethod
    def show_income(self):
        pass
