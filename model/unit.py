class Unit:
    _productivity_factor = 1

    def __init__(self):
        self.productivity = 0
        self.money = 0
        self.optimism = 0
    
    def Iterate(self):
        self.productivity += self._productivity_factor
