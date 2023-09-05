from model.economy import Economy
from model.unit import Unit

def test_Unit_constructor():
    economy = Economy()
    unit = Unit(economy)

    assert unit.productivity == 0
    assert unit.money == 100
    assert unit._economy == economy
    assert unit.goods_produced == 0
    assert unit.current_needs == 0

def test_Unit_live_one_cycle():
    economy = Economy()
    unit = Unit(economy)

    assert unit.productivity == 0
    assert unit.money == 100
    assert unit._economy == economy
    assert unit.goods_produced == 0
    assert unit.current_needs == 0

    unit.Iterate()

    assert unit.productivity > 0
    assert unit.money == 100
    assert unit._economy == economy
    assert unit.goods_produced > 0
    assert unit.current_needs > 0 
