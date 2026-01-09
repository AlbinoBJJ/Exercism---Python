def distance(strand_a, strand_b):
    #1  calcular o len de cada strand (se iguais, passa para o #2, se não , raise ValueError("Strands must be of equal length."))
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        #2 abrir um contador com valor 0
        counter = 0
        zipped_strands = zip(strand_a, strand_b)
        
        #3 iterar cada strand e verificar se os índices correspondem (talvez usar um zip(lista1, lista2))
        for a, b in zipped_strands:
            #4 se o índice corresponde, continue, se não, soma a contagem
            if a != b:
                counter += 1
    return counter
