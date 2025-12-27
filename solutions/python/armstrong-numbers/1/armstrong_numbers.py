def is_armstrong_number(number):
    num_to_string = str(number)
    power = len(num_to_string)
    str_list = list(num_to_string)
    int_list = [int(item) for item in str_list]
    powered_list = []
    for i in int_list:
        num = i ** power
        powered_list.append(num)
    total = sum(powered_list)
    return total == number
