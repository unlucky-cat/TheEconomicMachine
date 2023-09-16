from model.unit import Unit
from typing import List

class Economy:

    class Statistics:
        def __init__(self
                     , total_productivity = 0
                     , total_current_needs = 0
                     , total_goods_produced = 0
                     , total_reminders = 0
                     , total_money = 0
                     , total_units_count = 0
                     , total_food = 0):
            self.total_productivity = total_productivity
            self.total_current_needs = total_current_needs
            self.total_goods_produced = total_goods_produced
            self.total_reminders = total_reminders
            self.total_money = total_money
            self.total_units_count = total_units_count
            self.total_food = total_food

        def to_dict(self):
            return {
                'total_productivity': self.total_productivity,
                'total_current_needs': self.total_current_needs,
                'total_goods_produced': self.total_goods_produced,
                'total_reminders': self.total_reminders,
                'total_money': self.total_money,
                'total_units_count': self.total_units_count,
                'total_food': self.total_food,
            }


    def __init__(self, initial_units_count=1000):
        total_procuctivity = 0
        total_current_needs = 0
        total_goods_produced = 0
        total_reminders = 0
        total_money = 0
        total_count = 0
        total_food = 0
        self.units: List[Unit] = []

        # collecting all initial data from the created units
        for _ in range(initial_units_count):
            unit = Unit(self, self._on_unit_die)
            total_procuctivity += unit.productivity
            total_current_needs += unit.consumption
            total_goods_produced += unit.production
            total_reminders += unit.reminders
            total_money += unit.money
            total_count += 1
            total_food += unit.food
            self.units.append(unit)

        self.statistics = [
                Economy.Statistics(
                    total_procuctivity, 
                    total_current_needs,
                    total_goods_produced, 
                    total_reminders,
                    total_money,
                    total_count,
                    total_food
                )]

    def _on_unit_die(self, item: Unit):
        pass
        # self.units.remove(item)

    def iterate(self, x_times=1):
        for _ in range(x_times):
            total_procuctivity = 0
            total_current_needs = 0
            total_goods_produced = 0
            total_reminders = 0
            total_money = 0
            total_count = 0
            total_food = 0

            for unit in self.units:
                unit.iterate()
                if not unit.is_dead:
                    total_procuctivity += unit.productivity
                    total_current_needs += unit.consumption
                    total_goods_produced += unit.production
                    total_reminders += unit.reminders
                    total_money += unit.money
                    total_count += 1
                    total_food += unit.food
            
            self.statistics.append(
                Economy.Statistics(
                    total_procuctivity, 
                    total_current_needs,
                    total_goods_produced, 
                    total_reminders,
                    total_money,
                    total_count,
                    total_food
                )
            )
            

    @property
    def total_money(self):
        return self.statistics[-1].total_money     
    
    @property
    def total_productivity(self):
        return self.statistics[-1].total_productivity
    
    @property
    def total_goods_produced(self):
        return self.statistics[-1].total_goods_produced
    
    @property
    def total_units_count(self):
        return self.statistics[-1].total_units_count
    
    @property
    def total_reminders(self):
        return self.statistics[-1].total_reminders
    
    @property
    def total_current_needs(self):
        return self.statistics[-1].total_current_needs
