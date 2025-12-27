def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)

def total():
    squares = [2**power for power in range(64)]
    return sum(squares)