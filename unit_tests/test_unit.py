from model.economy import Economy
from model.unit import Unit

def test_Unit_constructor():
    economy = Economy(1)
    unit = economy.units[0]

    assert unit.productivity == 0
    assert unit.money == 100
    assert unit.economy == economy
    assert unit.production == 0
    assert unit.consumption == 0
    assert unit.reminders == 0
    assert unit.food > 0

def test_Unit_with_zero_food_dies():
    economy = Economy(1)
    unit = economy.units[0]
    unit.food = 0

    unit.iterate()

    assert unit.is_dead == True

def test_Unit_with_one_food_dies():
    economy = Economy(1)
    unit = economy.units[0]
    unit.food = 1

    unit.iterate()

    assert unit.is_dead == True

def test_Unit_live_one_cycle():
    economy = Economy(1)
    unit = economy.units[0]
    initial_food = unit.food

    assert unit.productivity == 0
    assert unit.money == 100
    assert unit.economy == economy
    assert unit.production == 0
    assert unit.consumption == 0
    assert unit.reminders == 0
    assert initial_food > 0

    unit.iterate()

    assert unit.productivity > 0
    assert unit.money == 100
    assert unit.economy == economy
    assert unit.production > 0
    assert unit.consumption > 0 
    assert unit.reminders == unit.production - unit.consumption
    assert unit.food == initial_food - 1
