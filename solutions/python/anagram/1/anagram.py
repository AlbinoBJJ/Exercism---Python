def find_anagrams(word, candidates):
    word_lower = word.casefold()
    print(word_lower)
    word_sorted = sorted(word_lower) 
    result = []
    for candidate in candidates:
        candidate_lower = candidate.casefold()
        if candidate_lower != word_lower:
            if sorted(candidate_lower) == word_sorted:
                result.append(candidate)   
    return result
