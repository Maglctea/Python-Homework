def rle_pack(string):
    buffer = string[0]
    result = ''
    count_symbol = 0

    for symbol in string:
        if symbol == buffer:
            count_symbol += 1
        else:
            result += f'{str(count_symbol)}{buffer}'
            buffer = symbol
            count_symbol = 1

    result += f'{str(count_symbol)}{buffer}'   
    return result

def rle_unpack(string):
    new_string = ""
    amount = ""

    for i in string:
        if i.isdigit():
            amount += i
        else:
            num = int(amount)
            new_string += num*i
            amount = ""

    return new_string

s = input('Введите строку для сжатия: ')
pack = rle_pack(s)
print('Сжатая строка', pack)

unpack = rle_unpack(pack)
print('Распакованная строка', unpack)
