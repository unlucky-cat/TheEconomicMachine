from model.unit import Unit


class Economy:

    def __init__(self, initial_units_count=1000):
        self._total_productivity_history = [0]
        self._units = self._spawn(initial_units_count)
    
    def _spawn(self, count):
        return [Unit(self) for _ in range(count)]
    
    def Iterate(self, x_times=1):
        for _ in range(x_times):
            for unit in self._units:
                unit.Iterate()

            self._total_productivity_history.append(self._calculate_total_procuctivity())
            
    def _calculate_total_procuctivity(self):
        summ = 0

        for unit in self._units:
            summ += unit.productivity

        return summ

    @property
    def total_money(self):
        summ = 0

        for unit in self._units:
            summ += unit.money

        return summ       
    
    @property
    def avg_money(self):
        summ = 0
        count = 0

        for unit in self._units:
            summ += unit.money
            count += 1

        return summ / count
    
    @property
    def total_productivity(self):
        return self._total_productivity_history[-1]