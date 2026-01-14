def factors(value):
    factor = []
    prime = 2
    num = value
    # this code would not be good for big numbers
    while num > 1:
        if num % prime == 0:
            factor.append(prime)
            num = num // prime
        else:
            prime += 1
    return factor
