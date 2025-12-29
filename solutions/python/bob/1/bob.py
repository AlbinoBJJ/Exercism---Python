def response(hey_bob):
    bob_dial = hey_bob.strip()
    if  bob_dial == '':
        return "Fine. Be that way!"
    elif bob_dial.endswith('?') and bob_dial.isupper():
        return "Calm down, I know what I'm doing!"
    elif bob_dial.isupper():
        return "Whoa, chill out!"
    elif bob_dial.endswith('?'):
        return "Sure."
    else:
        return "Whatever."