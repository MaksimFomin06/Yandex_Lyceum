equipment = {'tents': 2, 'food': 15, 'water': 3, 'fuel': 7}


def mountain_pass(my_equipment):
    missing = {}
    for item, needed in equipment.items():
        have = my_equipment.get(item, 0)
        if have < needed:
            missing[item] = needed - have
    
    return {'result': 'OK'} if not missing else missing