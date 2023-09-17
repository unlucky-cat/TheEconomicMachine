from model.economy import Economy

def test_Economy_with_zero_units():
    eco = Economy(0)
    eco.iterate(1)

def test_Economy_constructor_spawns_1000_units_by_default():
    eco = Economy()
    
    assert len(eco.units) == 1000

def test_Economy_iterate_one_time_with_dying_unit():
    eco = Economy(1)
    eco.units[0].food = 1
    eco.units[0].productivity_factor = 1
    #eco.units[0].productivity = 0
    eco.units[0].production = 0
    eco.units[0].consumption_factor = 1
    eco.units[0].consumption = 0

    eco.iterate()

    assert len(eco.units) == 1 , "unit should stay in the list after dying"
    assert eco.units[0].is_dead, "dead unit should be marked as dead"
    assert len(eco.statistics) == 2, "after one iteration there should be two statistical records - initial and from the first iteration"
    assert eco.statistics[0].total_units_count == 1, "there shoul be one unit initially"
    assert eco.statistics[1].total_units_count == 0, "there should be no units after the first iteration"
    assert sum([stat.total_money for stat in eco.statistics]) == 100


def test_Economy_iterate_one_time():
    initial_units_count = 10
    eco = Economy(initial_units_count)

    #assert eco.total_productivity == 0
    assert eco.total_money == 100 * initial_units_count
    assert eco.total_goods_produced == 0
    #assert eco.total_reminders == 0
    assert eco.total_current_needs == 0
    assert eco.total_units_count == initial_units_count

    eco.iterate()

    units_count = eco.statistics[1].total_units_count

    #assert eco.total_productivity > 0
    assert eco.total_money == 100 * units_count
    assert eco.total_goods_produced > 0
    assert eco.total_units_count == units_count
    #assert round(eco.total_reminders, 2) == round(eco.total_goods_produced - eco.total_current_needs, 2)
    assert eco.total_current_needs > 0
    
