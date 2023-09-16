import random
from model.item import Item
from model.bee import BasicEconomicEntity

class Unit(BasicEconomicEntity):

    def __init__(self, economy, on_death_callback = None, productivity_factor = -1, consumption_factor = -1):
        """productivity_factor is a value by which productivity grows
        productivity is a value by which production grows
        production is a speed at which value is produced per iteration"""
        
        super().__init__()
        self.productivity_factor = random.random() if productivity_factor == -1 else productivity_factor
        self.consumption_factor = random.random() if consumption_factor == -1 else consumption_factor
        self.economy = economy
        self.on_death_callback = on_death_callback

        self.productivity = 0
        self.reminders = 0
        self.money = 100
        self.food = random.randrange(1, 100)
        self.optimism = 0
        self.items = [Item()]
        self.is_dead = False
  
    def iterate(self):
        if self.is_dead: return
        
        sum_of_items_production = sum([item.production for item in self.items])
        sum_of_items_consumption = sum([item.consumption for item in self.items])

        self.productivity += self.productivity_factor
        self.production += (self.productivity + sum_of_items_production)
        self.consumption += (self.consumption_factor + sum_of_items_consumption)
        self.reminders += (self.production - self.consumption)

        self.food -= 1

        if self.food <= 0:
            self.food = 0
            self._die()

    def _die(self):
        self.is_dead = True

        if self.on_death_callback is not None:
            self.on_death_callback(self)