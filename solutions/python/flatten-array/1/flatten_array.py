def flatten(iterable):
    itens = []
    for item in iterable:
        if not isinstance(item, list) and item is not None:
            itens.append(item)
        elif isinstance(item, list):
            flattened_sublist = flatten(item)
            itens.extend(flattened_sublist)

    return itens

print(flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]))