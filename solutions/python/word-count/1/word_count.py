def count_words(sentence):
    clean_sentence = ''
    
    for char in sentence:
        if char == ',' or char == '_':
            clean_sentence += ' '
        elif char == "'" or char.isalnum() or char.isspace():
            clean_sentence += char
                
    
    words = clean_sentence.lower().split()
    
    words_count = {}
    
    for word in words:
        if word.startswith("'") or word.endswith("'"):
            clean_word = word.strip("'")
            words_count[clean_word] = words_count.get(clean_word, 0) + 1
        else:
            words_count[word] = words_count.get(word, 0) + 1
            
    return words_count