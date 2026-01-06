COLORS = [
        'black',  # 0
        'brown',  # 1
        'red',    # 2
        'orange', # 3
        'yellow', # 4
        'green',  # 5
        'blue',   # 6
        'violet', # 7
        'grey',   # 8
        'white'   # 9
    ]

def color_code(color):
    return COLORS.index(color)

def value(colors):
    num_str = [] # lista de números
    for color in colors: # loop para iterar as cores 
        char_str = color_code(color) # usa a função color_code() para pegar o índice da cor
        num_str.append(str(char_str)) # salva o índice da cor como um número na lista
        if len(num_str) == 3: #verifica se os três primeiros dígitos foram iterados e para o loop caso existam mais de três itens
            break
    main_value = int(''.join(num_str[:2])) # retorna o valor principal do resistor
    exponent = int(num_str[2]) # retorna a exponenciação
    return main_value, exponent

def label(colors):
    main_value, exponent = value(colors)
    resistor = main_value if exponent == 0 else main_value * 10 ** exponent

    K = 10**3
    M = 10**6
    G = 10**9
    T = 10**12

    if resistor < K:
        ohm_label = 'ohms'
    elif resistor < M:
        ohm_label = 'kiloohms'
        resistor //= K
    elif resistor < G:
        ohm_label = 'megaohms'
        resistor //= M
    else:
        ohm_label = 'gigaohms'
        resistor //= G

    return f'{resistor} {ohm_label}'

print(label(["yellow", "violet", "yellow"]))