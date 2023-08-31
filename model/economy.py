from model.unit import Unit


class Economy:

    def __init__(self, initial_units_count=1000):
        self._total_productivity_history = [0]
        self._total_goods_produced_history = [0]
        self._units = self._spawn(initial_units_count)
    
    def _spawn(self, count):
        return [Unit(self) for _ in range(count)]
    
    def Iterate(self, x_times=1):
        for _ in range(x_times):
            for unit in self._units:
                unit.Iterate()

            self._calculate_totals()
            
    def _calculate_totals(self):
        total_procuctivity = 0
        total_goods_produced = 0

        for unit in self._units:
            total_procuctivity += unit.productivity
            total_goods_produced += unit.goods_produced

        self._total_productivity_history.append(total_procuctivity)
        self._total_goods_produced_history.append(total_goods_produced)

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
    
    @property
    def total_goods_produced(self):
        return self._total_goods_produced_history[-1] 