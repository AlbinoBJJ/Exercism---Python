def rotate(text, key):
    text_list = [c for c in text]
    # translate
    from_this = 'abcdefghijklmnopqrstuvwxyz'
    to_this = from_this[key:] + from_this[:key]
    translated_text_list = []
    for char in text_list:
        if char.isupper():
            encode_table = str.maketrans(from_this.upper(), to_this.upper())
            translated_char = char.translate(encode_table)
            translated_text_list.append(translated_char)
        else:
            encode_table = str.maketrans(from_this, to_this)
            translated_char = char.translate(encode_table)
            translated_text_list.append(translated_char)
    return ''.join(translated_text_list)