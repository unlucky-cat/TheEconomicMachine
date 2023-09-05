from model.economy import Economy


def test_Economy_constructor_spawns_1000_units_by_default():
    eco = Economy()
    
    assert len(eco._units) == 1000

def test_Economy_iterate_one_time():
    eco = Economy()

    assert eco.total_productivity == 0
    assert eco.total_money == 100 * 1000
    assert eco.avg_money == 100 * 1000 / 1000
    assert eco.total_goods_produced == 0
    assert eco.avg_goods_produced == 0
    assert eco.total_current_needs == 0

    eco.Iterate()

    assert eco.total_productivity > 0
    assert eco.total_money == 100 * 1000
    assert eco.avg_money == 100 * 1000 / 1000
    assert eco.total_goods_produced > 0
    assert eco.avg_goods_produced > 0
    assert eco.total_current_needs > 0
    
