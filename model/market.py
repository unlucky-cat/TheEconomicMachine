from typing import List

class Market:
    class Request:
        def __init__(self, owner, action, amount, price):
            self.owner = owner
            self.action = action # buy or sell
            self.amount = amount
            self.price = price # per unit
            self.satisfaction_level = 'unsatisfied'
    
    def __init__(self, product):
        self.product = product
        self.requests: List[Market.Request] = []

    def submit(self, request):
        self.requests.append(request)

    @property
    def average_price(self):
        return sum([r.price for r in self.requests]) / len(self.requests)