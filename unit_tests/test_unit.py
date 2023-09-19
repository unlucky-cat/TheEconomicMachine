from collections import namedtuple
from model.unit import Unit

def test_Unit_constructor():
    Economy = namedtuple('Economy', [])
    economy = Economy()
    unit = Unit(economy)

    assert 0 <= unit.bare_productivity < 1
    assert 0 <= unit.consumption_factor < 1
    assert len(unit.items) == 1
    assert unit.money == 100
    assert unit.economy == economy
    assert unit.production == 0
    assert unit.consumption == 0
    assert 1 <= unit.leftovers <= 10

def test_Unit_calculations_for_one_iteration():
    Market = namedtuple('Market', ['average_price', 'submit'])
    market = Market(0.3, lambda request: True)
    Economy = namedtuple('Economy', ['food_market'])
    economy = Economy(market)

    unit = Unit(economy)
    unit.leftovers = 2 # [1:4]
    unit.bare_productivity = 0.2 # [0:1)
    unit.consumption_factor = 0.5 # [0:1)
    unit.items[0].productivity_bonus = 0.1 # [0:1)

    unit.iterate()

    assert unit.leftovers == 1.8
    assert unit.production == 0.3
    assert unit.consumption == 0.5

def test_Unit_with_zero_food_dies():
    pass

def test_Unit_with_one_food_dies():
    pass

def test_Unit_live_one_cycle():
    pass
