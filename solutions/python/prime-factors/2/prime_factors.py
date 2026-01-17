def factors(value):
    factor = []
    prime = 2
    num = value

    while prime ** 2 <= num:
        if num % prime == 0:
            factor.append(prime)
            num = num // prime
        else:
            if prime <= 4:
                prime += 1
            else:
                prime += 2

    if num > 1:
        factor.append(num)

    return factor
