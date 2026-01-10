def rows(letter):
    # tratamento do input
    letter_upper = letter.upper()

    # encontrando índice
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    target_index = letters.index(letter_upper) # índice da letra alvo

    # medade superior do diamante
    superior = []

    # metade superior do diamante
    for index in range(target_index +1 ):
        current_char = letters[index]
        current_index = index
        inner_spaces = ' ' * (current_index * 2 - 1) # espaços internos
        outter_spaces = ' ' * (target_index - current_index) # espaços externos

        if current_char == 'A': # se for a letra 'A'
            row = outter_spaces + current_char + outter_spaces # a linha não espaços internos
            superior.append(row) # adiciona a linha na parte superior do diamante
        else: # se não for 'A'
            row = outter_spaces + current_char + inner_spaces + current_char + outter_spaces # a linha tem espaços internos
            superior.append(row) # adiciona a linha na parte superior do diamante

    # medade inferior do diamante
    if target_index != 0: # verifica a necessidade de fatiamento, caso 'A', retorna superior sem extenção da lista
        inferior = superior[target_index - 1::-1] # faz o slice invertido da parte superior e retira a última letra
        superior.extend(inferior) # extende as listas
    return superior