def prime(number):
    if number < 1:
        raise ValueError('there is no zeroth prime')
    prime_numbers_list = []
    candidate_prime_number = 2
    while len(prime_numbers_list) < number:
        is_prime_flag = True
        for num in prime_numbers_list:
            if num ** 2 > candidate_prime_number:
                break
            divisor_check = candidate_prime_number % num == 0
            if divisor_check:
                is_prime_flag = False
                break
        if is_prime_flag:
            prime_numbers_list.append(candidate_prime_number)
        if candidate_prime_number < 3:
            candidate_prime_number += 1
        else:
            candidate_prime_number += 2
    return prime_numbers_list[-1]