class TextualString:
    def find_expressions(text,start,end,start_skip = 0,end_skip = 0):
        text = str(text)
        start = str(start)
        end = str(end)
        start_len = len(start)
        end_len = len(end)
        count = min([text.count(start),text.count(end)])
        interval = [text.find(start,0),text.find(start,0) + start_len]
        result = []
        if count == 0 : return result
        for index in range(count):
            interval = [text.find(start,interval[0]),text.find(end,interval[1])]
            if -1 in interval : break
            new_found = text[interval[0] + start_skip : interval[1] + end_len + end_skip]
            result.append(new_found)
            interval = [text.find(start,interval[0] + 1),text.find(start,interval[0] + 1) + start_len]
        return result

# with open("path", 'r') as file:
#     x = file.read()
#     y = TextualString.find_expressions(x,'href=\"','\"',17,-5)
#     for i in y:
#         print(i)
