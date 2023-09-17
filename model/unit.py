import random
from model.item import Item
from model.economy import Economy
from model.market import Market
from model.bee import BasicEconomicEntity

class Unit(BasicEconomicEntity):

    def __init__(self, economy: Economy, on_death_callback = None, bare_productivity = -1, consumption_factor = -1):
        """productivity is a value by which production grows
        base_productivity is a bare human productivity (no tools used),
        so productivity = bare_productivity + sum(tools.productivity)
        production is a speed at which value is produced per iteration
        
        Production refers to conversion of raw materials into final product. 
        eg:crude oil into petrol, diesel etc 
        whereas consumption refers to making use of them. 
        eg:as a fuel for vehicles"""
        
        super().__init__()
        self.bare_productivity = random.random() if bare_productivity == -1 else bare_productivity
        self.consumption_factor = random.random() if consumption_factor == -1 else consumption_factor
        self.economy = economy
        self.on_death_callback = on_death_callback

        self.money = 100
        self.leftovers = random.randrange(1, 10)
        #self.optimism = 0
        self.items = [Item()]
        self.is_dead = False
  
    def iterate(self):
        if self.is_dead: return
        
        sum_of_items_productivity_bonus = sum([item.productivity_bonus for item in self.items])

        self.production = round((self.bare_productivity + sum_of_items_productivity_bonus), 2)
        self.consumption = self.consumption_factor

        diff = (self.production - self.consumption)
        self.leftovers += round(diff, 2)

        # i'm still alive, have money and have negative diff - need to buy food or tools
        if self.leftovers > 0 and diff < 0 and self.money > 0:
            avg_price = self.economy.food_market.average_price
            avg_price -= avg_price * 0.1
            self.economy.food_market.submit(Market.Request(self, 'buy', 4, avg_price))


        # i have extra leftovers and positive diff - can sell
        if self.leftovers > 10 and diff > 0:
            avg_price = self.economy.food_market.average_price
            avg_price += avg_price * 0.1
            self.economy.food_market.submit(Market.Request(self, 'sell', 5, avg_price))


        if self.leftovers <= 0:
            self.leftovers = 0
            self._die()

    def _die(self):
        self.is_dead = True

        if self.on_death_callback is not None:
            self.on_death_callback(self)