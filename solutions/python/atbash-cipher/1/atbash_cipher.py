def encode(plain_text):
    # everything lowercase
    lower_text = plain_text.lower()
    # translate
    from_this = 'abcdefghijklmnopqrstuvwxyz'
    to_this = 'zyxwvutsrqponmlkjihgfedcba'
    encode_table = str.maketrans(from_this, to_this) 
    # filter: spaces, periods, commas
    clean_text = lower_text.translate(encode_table).replace(' ', '')
    char_list = []
    for char in clean_text:
        if char.isalnum():
            char_list.append(char)
    clean_string = ''.join(char_list)
    # groups of five
    five_chars_blocks = []
    for index in range(0, len(clean_string), 5):
        block = clean_string[index:index + 5]
        five_chars_blocks.append(block)
    # join groups of five with ' ' 
    return ' '.join(five_chars_blocks)

def decode(ciphered_text):
    lower_text = ciphered_text.lower()
    from_this = 'zyxwvutsrqponmlkjihgfedcba'
    to_this = 'abcdefghijklmnopqrstuvwxyz'
    encode_table = str.maketrans(from_this, to_this)
    return ciphered_text.translate(encode_table).replace(' ','')