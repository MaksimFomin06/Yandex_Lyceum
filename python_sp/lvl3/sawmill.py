def sawmill(*args, part=None, order=False):
    parts = []
    for wood in args:
        for i in range(0, len(wood), part):
            chunk = wood[i:i + part]
            if len(chunk) == part:
                parts.append(chunk)
    
    if order:
        parts.sort(reverse=True)
    else:
        parts.sort()
    
    return parts