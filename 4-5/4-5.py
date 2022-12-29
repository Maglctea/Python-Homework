# Программа работает только с одночленами, множеными на X или обычные числа

operators = {'*': 0, '**': {}, None: {}}

def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def serialisation(text_list):
    analisator = {'*': 0, '**': {}, '': 0}
    for text in text_list:
        if text.count('*') == 3:            
            sqr = int(text.split(' ** ')[1])
            if sqr in analisator['**']:
                analisator['**'][sqr] += int(text.split(' * ')[0])
            else:
                analisator['**'][sqr] = int(text.split(' * ')[0])
        elif text.count('*') == 1:
            # print(text.split(' * '))
            analisator['*'] += int(text.split(' * ')[0])
        elif text == '-x':
            analisator['*'] -= 1
        elif text == 'x':
            analisator['*'] += 1
        else:
            analisator[''] += int(text)
    return analisator

def deserialisation(text_dict):
    result_list = []
    for key in text_dict['**']:
        if text_dict['**'][key] != 0:
            result_list.append(f"{text_dict['**'][key]} * x ** {key}")
    if text_dict['*'] != 0:
        result_list.append(f"{text_dict['*']} * x")
    if text_dict[''] != 0:
        result_list.append(f"{text_dict['']}")
    result_str = ' + '.join(result_list)
    result_str = result_str.replace(' + -', ' - ')
    return result_str

def sum_text(*args):
    sum_text = ' + '.join(args)
    sum_text = sum_text.replace(' + -', ' - ')
    return sum_text

text1 = read_file('input1.txt')
print('Выражение 1:\n', text1)
text2 = read_file('input2.txt')
print('Выражение 2:\n', text2)

sum_text = sum_text(text1, text2)
print('Сумма выражений до упрощения:\n', sum_text)
sum_text = sum_text.replace(' - ', ' + -')


analis_list = serialisation(sum_text.split(' + '))
sum_text_optimal = deserialisation(analis_list)

print('Сумма выражений после упрощения:\n', sum_text_optimal)

with open('output.txt', "w", encoding="utf-8") as file:
    file.write(sum_text_optimal)
