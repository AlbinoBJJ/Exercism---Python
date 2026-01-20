def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")        
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    index = 0
    fatias = []
    for slc in series:
        fatia = series[index : index + length]
        if len(fatia) == length:
            fatias.append(fatia)
        index += 1
    return fatias