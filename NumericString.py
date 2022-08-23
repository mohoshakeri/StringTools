class NumericString:
    
    def toEnglish(text):
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
        newtext = list(text)
        for index,letter in enumerate(newtext):
            for num in FA_EN:
                if letter == num:
                    newtext[index] = FA_EN[num]
                    break
                
        return "".join(newtext)
    
    def compart(number):
        number = list(reversed(str(number)))
        newText = ""
        for i in range((len(number)//3)+1):
            if len(number) == 3 : return "".join(reversed(number))
            count = 0 + (3 * i)
            compart = number[count:count+3]
            if i == 0 or (i == list(range((len(number)//3)+1))[-1] and (len(number) % 3 == 0)):
                newText = f'{newText}{"".join(compart)}'
            else:
                newText = f'{newText},{"".join(compart)}'
            
        return "".join(reversed(newText))
