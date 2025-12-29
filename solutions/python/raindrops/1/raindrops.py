def convert(number):
    pling = number % 3 == 0
    plang = number % 5 == 0
    plong = number % 7 == 0
    raindrop = ''
    if pling:
        raindrop += 'Pling'
    if plang:
        raindrop += 'Plang'
    if plong:
        raindrop += 'Plong'
    if not raindrop:
        raindrop = f'{number}'
    return raindrop
