def egg_count(display_value):
    remainder_counter = 0
    actual_quotient = display_value
    while actual_quotient > 0:
        division = actual_quotient // 2
        remainder = actual_quotient % 2
        actual_quotient = division
        remainder_counter += remainder
    return remainder_counter
