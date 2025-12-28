def steps(number):
    number_of_steps = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
                    
        if number % 2 == 0:
            number //= 2
            number_of_steps += 1
        else:
            number *= 3
            number += 1
            number_of_steps += 1

    return number_of_steps


print(steps(2))
