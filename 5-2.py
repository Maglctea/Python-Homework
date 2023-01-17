def print_menu():
    print('1). Новая игра.')
    print('2). Выход.')

    choice = int(input())
    while choice > 2 or choice < 1:
        choice = int(input('Некорректный ввод!\n'))
    return choice

def printTable(table: list):
    def get_symbol(id):
        if id == 1:
            return '❌'
        elif id == 2:
            return '⭕'
        else:
            return '🔲'
    print()
    for row in table:
        for pos in row:
            print(get_symbol(pos), end='')
        print()

def new_game(table: list):
    table.clear()
    for i in range(3):
        table.append([0, 0, 0])

def set_symbol(table, row, pos, id):
    row -= 1
    pos -= 1
    if 0 <= row < len(table) and 0 <= pos < len(table) and table[row][pos] == 0 :
        table[row][pos] = id
        return True
    else:
        return False

def check_win(table):
    # Проверка строк
    count_null = 0
    for row in table:
        count_null += row.count(0)
        if row.count(1) == 3: 
            return (True, 1)
        elif row.count(2) == 3:
            return (True, 2)
            
    # Проверка столбцов 
    for pos in range(len(table)):
        count_o = 0
        count_x = 0
        for row in range(len(table)):
            if table[row][pos] == 1:
                count_x += 1
            elif table[row][pos] == 2:
                count_o += 1
            # Анализ результата
            if count_x == 3:
                return (True, 1)
            elif count_o == 3:
                return (True, 2)

    # Проверка диагоналей
    count_o = 0
    count_x = 0
    for pos in range(len(table)):
        if table[len(table) - pos - 1][pos] == 1:
            count_x += 1
        elif table[len(table) - pos - 1][pos] == 2:
            count_o += 1
            # Анализ результата
            if count_x == 3:
                return (True, 1)
            elif count_o == 3:
                return (True, 2)

    count_o = 0
    count_x = 0
    for pos in range(len(table)):
        if table[pos][pos] == 1:
            count_x += 1
        elif table[pos][pos] == 2:
            count_o += 1
        # Анализ результата
        if count_x == 3:
            return (True, 1)
        elif count_o == 3:
            return (True, 2)
    
    if count_null == 0:
        return (True, 3)

    return (False,)

game_map = []
while print_menu() != 2:
    # Запуск игры
    new_game(game_map)
    stage = 0
    while not check_win(game_map)[0]:
        printTable(game_map)
        stage += 1        
        if stage % 2 == 1:
            x, y = map(int, input('Ход 1 игрока. Введите координату в формате X Y\n').split())
            while not set_symbol(game_map, y, x, 1):
                x, y = map(int, input('Неверный ввод! Введите координату в формате X Y. Например 1 2\n').split())

        else:
            x, y = map(int, input('Ход 2 игрока. Введите координату в формате X Y\n').split())
            while not set_symbol(game_map, y, x, 2):
                x, y = map(int, input('Неверный ввод! Введите координату в формате X Y. Например 1 2\n').split())

    winer = check_win(game_map)[1]
    if winer == 3:
        print('Ничья')
    else:
        print(f'Победил игрок {winer}')


