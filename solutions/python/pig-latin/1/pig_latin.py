def rule1(word):
        new_word = word + 'ay'
        return new_word

def rule_2_3_4(word):
    for i, letter in enumerate(word):
        if letter.lower() in "aeiou" or (letter.lower() == 'y' and i > 0):
            vowel_index = word[i]
            if word[i] == 'u' and word[i-1] == 'q' and i > 0:
                new_word = word[i+1:] + word[:i+1] + 'ay'
                return new_word
            else:
                new_word = word[i:] + word[:i] + 'ay'
                return new_word
    else:
        new_word = word
        return new_word

def translate(text):
    word_list = text.split()
    new_words = []
    start_with = 'a', 'e', 'i', 'o', 'u', 'xr', 'yt'
    for word in word_list:
        if word.startswith(start_with):
            translated_word = rule1(word)
            new_words.append(translated_word)
        else:
            translated_word = rule_2_3_4(word)
            new_words.append(translated_word)

    return ' '.join(new_words)
