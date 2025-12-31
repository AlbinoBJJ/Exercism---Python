def is_isogram(string):
    clean_string = []
    for char in string.lower():
        if char.isalpha():
            clean_string.append(char)
    return len(clean_string) == len(set(clean_string))
