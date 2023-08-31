import random


class Unit:

    def __init__(self, economy):
        self._productivity_factor = random.random()
        self._economy = economy
        self._productivity_history = [0]

        self.money = 100
        self.optimism = 0
        self.goods_produced = 0
  
    def Iterate(self):
        self._productivity_history.append(self.productivity + self._productivity_factor)
        self.goods_produced += self.productivity

    @property
    def productivity(self):
        return self._productivity_history[-1]
