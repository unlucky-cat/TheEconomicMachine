from model.unit import Unit


class Economy:

    class Statistics:
        def __init__(self
                     , total_productivity = 0
                     , total_goods_produced = 0
                     , avg_goods_produced = 0
                     , total_money = 0
                     , avg_money = 0):
            self.total_productivity = total_productivity
            self.total_goods_produced = total_goods_produced
            self.avg_goods_produced = avg_goods_produced
            self.total_money = total_money
            self.avg_money = avg_money


    def __init__(self, initial_units_count=1000):
        total_procuctivity = 0
        total_goods_produced = 0
        total_money = 0
        count = 0
        self._units = []

        for _ in range(initial_units_count):
            unit = Unit(self)
            total_procuctivity += unit.productivity
            total_goods_produced += unit.goods_produced
            total_money += unit.money
            count += 1
            self._units.append(unit)

        self._statistics = [
                Economy.Statistics(
                    total_procuctivity, 
                    total_goods_produced, 
                    total_goods_produced / count,
                    total_money,
                    total_money / count
                )]

    
    def Iterate(self, x_times=1):
        for _ in range(x_times):
            total_procuctivity = 0
            total_goods_produced = 0
            total_money = 0
            count = 0

            for unit in self._units:
                unit.Iterate()
                total_procuctivity += unit.productivity
                total_goods_produced += unit.goods_produced
                total_money += unit.money
                count += 1
            
            self._statistics.append(
                Economy.Statistics(
                    total_procuctivity, 
                    total_goods_produced, 
                    total_goods_produced / count,
                    total_money,
                    total_money / count
                )
            )
            

    @property
    def total_money(self):
        return self._statistics[-1].total_money     
    
    @property
    def avg_money(self):
        return self._statistics[-1].avg_money
    
    @property
    def total_productivity(self):
        return self._statistics[-1].total_productivity
    
    @property
    def total_goods_produced(self):
        return self._statistics[-1].total_goods_produced
    
    @property
    def avg_goods_produced(self):
        return self._statistics[-1].avg_goods_produced