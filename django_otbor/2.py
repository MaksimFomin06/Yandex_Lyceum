def stairs(objects):
    result = []
    object_index = 0
    position_in_object = 0

    while objects:
        current_object = objects[object_index]

        try:
            element = current_object[position_in_object]
        except IndexError:
            object_index = (object_index + 1) % len(objects)
            position_in_object = 0
            continue

        if element % 2 == 0:
            object_index = (object_index + 1) % len(objects)
            position_in_object = 0
        else:
            result.append(element)
            position_in_object += 1

        if position_in_object >= len(current_object):
            objects.pop(object_index)
            object_index %= len(objects)

    return result