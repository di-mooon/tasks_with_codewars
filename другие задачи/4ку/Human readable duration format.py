def format_duration(seconds):
    if seconds == 0: return 'now'
    dictionary = {'years': seconds // 31536000, 'days': seconds % 31536000 // 86400,
                  'hours': seconds % 86400 // 3600, 'minutes': seconds % 3600 // 60,
                  'seconds': seconds % 60}

    string_output = [f'{value} {key[:-1]}' if value == 1 else f'{value} {key}'
                     for key, value in dictionary.items() if value != 0]
    if len(string_output) >= 2:
        string_output[-1] = 'and ' + string_output[-1]

    return ', '.join(string_output).replace(', and', ' and')
