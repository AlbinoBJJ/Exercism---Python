def is_pangram(sentence):
    sentence = sentence.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in sentence:
            return False
    else:
        return True
