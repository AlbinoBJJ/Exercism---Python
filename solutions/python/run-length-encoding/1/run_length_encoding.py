def decode(string):
    decoded = ''
    count_string = ''

    for char in string:
        if char.isdigit():
            count_string += char
        else:
            if count_string == '':
                decoded += char
            else:
                decoded += (char * (int(count_string)))
                count_string = ''
    return decoded


def encode(string):
    if not string:
        return ''
    
    encoded = ''
    counter = 1

    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            counter += 1
        else:
            if counter == 1:
                encoded += f'{string[index]}'
                counter = 1
            else:
                encoded += f'{counter}{string[index]}'
                counter = 1
    if counter == 1:
        encoded += f'{string[index + 1]}'
    else:
        encoded += f'{counter}{string[index + 1]}'
    return encoded
