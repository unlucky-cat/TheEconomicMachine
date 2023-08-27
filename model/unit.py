import random


class Unit:

    def __init__(self, economy):
        self._productivity_factor = random.random()
        self._economy = economy
        self._productivity_history = [0]

        self.money = 0
        self.optimism = 0
  
    def Iterate(self):
        self._productivity_history.append(self.productivity + self._productivity_factor)

    @property
    def productivity(self):
        return self._productivity_history[-1]
