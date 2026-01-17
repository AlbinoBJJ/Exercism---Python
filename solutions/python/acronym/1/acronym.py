def abbreviate(words):
    acronym = []
    clean_words = words.replace('-', ' ').replace("'",'').lower().title()
    for char in clean_words:
        if char.isupper():
            acronym.append(char)
    return ''.join(acronym)