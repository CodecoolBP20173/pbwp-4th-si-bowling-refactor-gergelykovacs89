def spare_score(current_throw, last_throw):
    if current_throw == '/':
        return 10 - get_value(last_throw)
    else:
        return get_value(current_throw)


def score(game):
    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):

        result += spare_score(game[i], game[i-1])

        if frame < 10 and get_value(game[i]) == 10:
            result += get_value(game[i+1])
            if game[i] == 'X' or game[i] == 'x':
                result += spare_score(game[i+2], game[i+1])

        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1

    return result


def get_value(char):
    if char in "123456789":
        return int(char)
    elif char.upper() in 'X/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
