COLORS = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]

def color_code(color):
    return COLORS.index(color)

def colors():
    return COLORS

def value(colors):
    num_str = []
    for color in colors:
        char_str = color_code(color)
        num_str.append(str(char_str))
        if len(num_str) == 2:
            break

    return int(''.join(num_str))
print(value(["black", "brown"]))