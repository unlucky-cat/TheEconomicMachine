import random


class Unit:

    def __init__(self, economy):
        self._productivity_factor = random.random()
        self._needs_growing_factor = random.random()
        self._economy = economy
        # self._needs_satisfaction_history = [0]
        self._history_data = {
            "productivity": [0],
            "goods_produced": [0],
            "needs_growing": [0],
        }

        self.money = 100
        self.optimism = 0
        self.goods_produced = 0
  
    def Iterate(self):
        productivity = self.productivity + self._productivity_factor
        self._history_data["productivity"].append(productivity)
        self.goods_produced += productivity
        self._history_data["goods_produced"].append(self.goods_produced)

        current_needs = self.current_needs + self._needs_growing_factor
        self._history_data["needs_growing"].append(current_needs)


    @property
    def productivity(self):
        return self._history_data["productivity"][-1]

    @property
    def current_needs(self):
        return self._history_data["needs_growing"][-1]