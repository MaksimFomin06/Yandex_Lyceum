def stairs(objects):
    result = []
    index = 0

    while objects:
        current_object = objects[index % len(objects)]

        try:
            element = next(current_object)
        except StopIteration:
            del objects[index % len(objects)]
            continue
            
        if element % 2 == 0:
            index += 1
        else:
            result.append(element)
    
    return set(result)