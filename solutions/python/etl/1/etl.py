def transform(legacy_data):
    new_dict = {}
    for data in legacy_data:
        for letter in legacy_data[data]:
            new_dict[letter.lower()] = new_dict.get(data, data)
    return dict(sorted(new_dict.items()))
