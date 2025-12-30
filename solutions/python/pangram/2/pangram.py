def is_pangram(sentence):
    sentence = sentence.lower().strip('",.;:~^´[]=-+_\|/?!#@$%¨&*()')
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in sentence:
            return False
    else:
        return True
