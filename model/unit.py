import random


class Unit:

    def __init__(self, economy):
        self._productivity_factor = random.random()
        self._economy = economy
        self._productivity_history = [0]
        self._goods_produced_history = [0]

        self.money = 100
        self.optimism = 0
        self.goods_produced = 0
  
    def Iterate(self):
        productivity = self.productivity + self._productivity_factor
        self._productivity_history.append(productivity)
        self.goods_produced += productivity
        self._goods_produced_history.append(self.goods_produced)

    @property
    def productivity(self):
        return self._productivity_history[-1]

