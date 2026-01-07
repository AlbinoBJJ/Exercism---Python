COLORS = [ # constante: lista de cores para as três primeiras listras do resistor
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

TOLERANCE = [ # constante: lista de cores para a listra de tolerância do resistor
    ('grey', 0.05),
    ('violet', 0.1),
    ('blue', 0.25),
    ('green', 0.5),
    ('brown', 1),
    ('red', 2),
    ('gold', 5),
    ('silver', 10)
]

def color_code(color): # acha e retorna o valor das cores para a função value através do índice das cores na lista
    return COLORS.index(color)


def tolerance_label(colors): # acha o valor de tolerância
    for color, value in TOLERANCE:
        if colors[-1] in color:
            return f'±{value}%'

def value(colors):
    num_str = [] # lista de números
    for color in colors: # loop para iterar as cores 
        char_str = color_code(color) # usa a função color_code() para pegar o índice da cor
        num_str.append(str(char_str)) # salva o índice da cor como um número na lista
    
    if len(num_str) <4:
        exponent = 0
        main_value = int(''.join(num_str[:2])) # retorna o valor principal do resistor
    elif len(num_str) == 4:
        exponent = int(num_str[-2]) # retorna a exponenciação
        main_value = int(''.join(num_str[:2])) # retorna o valor principal do resistor
    else:
        main_value = int(''.join(num_str[:3])) # retorna o valor principal do resistor
        exponent = int(num_str[-2]) # retorna a exponenciação
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
        resistor /= K
    elif resistor < G:
        ohm_label = 'megaohms'
        resistor /= M
    else:
        ohm_label = 'gigaohms'
        resistor /= G

    if resistor - int(resistor) == 0:
        return int(resistor), ohm_label
    return resistor, ohm_label

def resistor_label(colors):
    resistor, ohm_label = label(colors)
    if len(colors) <= 3:
        return f'0 {ohm_label}'
    return f'{resistor} {ohm_label} {tolerance_label(colors)}'