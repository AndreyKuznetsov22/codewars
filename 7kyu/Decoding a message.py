def decode(message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    message = list(message)
    for i in range(len(message)):
        if message[i] in alpha:
            message[i] = alpha[-1 * (alpha.index(message[i]) + 1)]
    return ''.join(message)