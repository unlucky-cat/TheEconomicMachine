from model.economy import Economy


def test_Economy_constructor_spawns_1000_units_by_default():
    eco = Economy()
    
    assert len(eco.units) == 1000

def test_Economy_iterate_one_time():
    eco = Economy()

    assert eco.GetTotalProductivity() == 0

    eco.Iterate()

    assert eco.GetTotalProductivity() == 1000