class NumericString:
    
    def to_English(text):
        FA_EN = {
            '۰' : '0',
            '۱' : '1',
            '۲' : '2',
            '۳' : '3',
            '۴' : '4',
            '۵' : '5',
            '۶' : '6',
            '۷' : '7',
            '۸' : '8',
            '۹' : '9',
        }
        text = str(text)
        new_text = list(text)
        for index,letter in enumerate(new_text):
            for num in FA_EN:
                if letter == num:
                    new_text[index] = FA_EN[num]
                    break
                
        return "".join(new_text)
    
    def compart(number):
        number = list(reversed(str(number)))
        new_text = ""
        for i in range((len(number)//3)+1):
            if len(number) == 3 : return "".join(reversed(number))
            count = 0 + (3 * i)
            compart = number[count:count+3]
            if i == 0 or (i == list(range((len(number)//3)+1))[-1] and (len(number) % 3 == 0)):
                new_text = f'{new_text}{"".join(compart)}'
            else:
                new_text = f'{new_text},{"".join(compart)}'
            
        return "".join(reversed(new_text))
