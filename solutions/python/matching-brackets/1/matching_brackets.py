def is_paired(input_string):
    # o dicionário mapeia a abertura (chave) ao fechamento (valor)
    pairs = {'(': ')', '[': ']', '{': '}'}
    pile = []

    for char in input_string:
        # se for uma abertura, guardamos na pilha
        if char in pairs.keys():
            pile.append(char)
        
        # Se for um fechamento
        elif char in pairs.values():
            # Se a pilha estiver vazia, fechou algo que não abriu
            if not pile:
                return False
            
            # Removemos o último que abriu
            opening = pile.pop()
            
            # Se o char atual não for o fechamento esperado para aquela abertura
            if char != pairs[opening]:
                return False
                
    # No final, a pilha deve estar vazia (tudo que abriu, fechou)
    return len(pile) == 0
            
