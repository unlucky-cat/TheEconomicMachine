from model.unit import Unit

def test_Unit_constructor():
    unit = Unit()

    assert unit.productivity == 0
    assert unit.money == 0

