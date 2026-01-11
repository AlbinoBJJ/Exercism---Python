def find(search_list, value):
    lower_index = 0
    higher_index = len(search_list) - 1
    
    if len(search_list) <= 0:
        raise ValueError("value not in array")
    elif value > search_list[-1]:
        raise ValueError("value not in array")
    elif value < search_list[0]:
        raise ValueError("value not in array")        
    
    while lower_index <= higher_index:
        mid_index = (lower_index + higher_index) // 2
        if value == search_list[mid_index]:
            return mid_index
        elif value < search_list[mid_index]:
            higher_index = mid_index - 1
        else:
            lower_index = mid_index + 1
    if mid_index != value:
        raise ValueError("value not in array")
    return mid_index