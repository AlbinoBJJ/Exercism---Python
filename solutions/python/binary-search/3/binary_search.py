def find(search_list, value):
    lower_index = 0
    higher_index = len(search_list) 
    
    while lower_index < higher_index:
        mid_index = (lower_index + higher_index) // 2
        if value == search_list[mid_index]:
            return mid_index
        elif value < search_list[mid_index]:
            higher_index = mid_index
        else:
            lower_index = mid_index + 1
    raise ValueError("value not in array")