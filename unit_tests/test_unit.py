from model.economy import Economy
from model.unit import Unit

def test_Unit_constructor():
    economy1 = Economy()
    unit1 = Unit(economy1)

    assert unit1.productivity == 0
    assert unit1.money == 0
    assert unit1._economy == economy1

