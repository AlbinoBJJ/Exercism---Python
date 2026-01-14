def square_of_sum(number):
    if number != 1:
        numbers = sum([num for num in range(1 , number + 1)])
    else:
        numbers = number
    return numbers ** 2


def sum_of_squares(number):
    if number != 1:
        return sum([num ** 2 for num in range(1 , number + 1)])
    return number

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
