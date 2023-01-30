"""
Создайте программу для игры в ""Крестики-нолики"" в телеграмме. Игра реализуется в терминале, игроки ходят поочередно,
необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента,
каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка,
на которую мы хотим поставить крестик или нолик,
и проверку на победу(стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
"""
import telebot
from telebot import types

TOKEN = 'ВАШ ТОКЕН'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def print_menu(message):
    button = types.KeyboardButton('Новая игра')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(button)
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)


def printTable(message, table: list):
    def get_symbol(id):
        if id == 1:
            return '❌'
        elif id == 2:
            return '⭕'
        else:
            return '🔲'

    table_str = ''
    for row in table:
        for pos in row:
            table_str += get_symbol(pos)
        table_str += '\n'
    bot.send_message(message.chat.id, table_str)


def new_game(table: list):
    table.clear()
    for i in range(3):
        table.append([0, 0, 0])


def set_symbol(message: types.Message, table, stage, player_number):
    map_list = message.text.split()
    try:
        pos = int(map_list[0]) - 1
        row = int(map_list[1]) - 1
    except:
        msg = bot.reply_to(message, 'Неверный ввод! Введите координату в формате X Y.\nНапример: 1 2')
        bot.register_next_step_handler(msg, set_symbol, table, stage, player_number)
        return

    if len(table) > row >= 0 == table[row][pos] and 0 <= pos < len(table):
        table[row][pos] = player_number
        game_controller(message, table, stage)
    else:
        msg = bot.reply_to(message, 'Клетка уже занята или вне диапазона! Попробуйте снова')
        bot.register_next_step_handler(msg, set_symbol, table, stage, player_number)
        return


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


@bot.message_handler(content_types=['text'])
def menu_controller(message: types.Message):
    if message.text == 'Новая игра':
        game_map = []
        new_game(game_map)
        game_controller(message, game_map, 0)


def game_controller(message: types.Message, game_map, stage):
    printTable(message, game_map)
    if not check_win(game_map)[0]:
        stage += 1
        if stage % 2 == 1:
            bot.send_message(message.chat.id, 'Ход 1 игрока. Введите координату в формате X Y\n')
            bot.register_next_step_handler(message, set_symbol, game_map, stage, 1)
        else:
            bot.send_message(message.chat.id, 'Ход 2 игрока. Введите координату в формате X Y\n')
            bot.register_next_step_handler(message, set_symbol, game_map, stage, 2)
    else:
        winer = check_win(game_map)[1]
        if winer == 3:
            bot.send_message(message.chat.id, 'Конец игры! Ничья')
        else:
            bot.send_message(message.chat.id, f'Конец игры! Победил игрок {winer}')
        print_menu(message)


bot.infinity_polling()
