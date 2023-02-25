import re


def zarinpal_authority(code):
    index = 0
    for char in code:
        if char == '0' or char == 'A':
            index += 1
            continue
        else:
            break
    code = list(code)
    result = ''.join(code[index:])
    return result

def persian_valid(input_string):
    persian_letters_pattern = re.compile(r'^[\u0621-\u06CC\s]+$')
    return bool(persian_letters_pattern.match(input_string) and not any(char.isdigit() for char in input_string))

def del_spaces(text):
    text = str(text)
    new_text = text.replace(" ","")
    return new_text