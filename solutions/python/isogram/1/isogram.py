def is_isogram(string):
    clean_string = []
    for char in string.lower():
        if char.isalpha():
            clean_string.append(char)
    if len(clean_string) == len(set(clean_string)):
        return True
    else:
        return False