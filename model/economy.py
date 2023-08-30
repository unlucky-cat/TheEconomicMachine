from model.unit import Unit


class Economy:
    def __init__(self, initial_units_count=1000):
        self.units = self._spawn(initial_units_count)
    
    def _spawn(self, count):
        return [Unit() for _ in range(count)]
    
    def Iterate(self):
        for unit in self.units:
            unit.Iterate()

    @property
    def total_money(self):
        summ = 0

        for unit in self.units:
            summ += unit.money

        return summ       
    
    @property
    def avg_money(self):
        summ = 0
        count = 0

        for unit in self.units:
            summ += unit.money
            count += 1

        return summ / count

    def GetTotalProductivity(self):
        summ = 0

        for unit in self.units:
            summ += unit.productivity

        return summ