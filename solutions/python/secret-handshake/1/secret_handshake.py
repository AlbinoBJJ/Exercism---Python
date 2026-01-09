def commands(binary_str):
    actions = [
        'wink', # 00001
        'double blink', # 00010
        'close your eyes', #00100
        'jump' # 01000
        # 10000 = Reverse the order of the operations in the secret handshake.
    ]

    command_list = []
    
    if binary_str[-1] == '1':
        command_list.append(actions[0])
    if binary_str[-2] == '1':
        command_list.append(actions[1])
    if binary_str[-3] == '1':
        command_list.append(actions[2])
    if binary_str[-4] == '1':
        command_list.append(actions[3])
    if binary_str[-5] == '1':
        command_list.reverse()
        
    return command_list
