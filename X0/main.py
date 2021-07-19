import time
def greeting():
    # приветствие в игре
    print("--------------------------------------------")
    print("  Добро пожаловать в игру крестики-нолики!  ")
    print("--------------------------------------------")
    time.sleep(1)

def invite():
    # знакомство с игроками
    print("  Давайте знакомиться! ")
    global pl_one, pl_one_name
    global pl_two, pl_two_name
    pl_one_name = input('  Игрок 1 - ')
    pl_two_name = input('  Игрок 2 - ')
    if pl_one_name[0].upper() == pl_two_name[0].upper():
        pl_one = 'X'
        pl_two = '0'
    else:
        pl_one = pl_one_name[0].upper()
        pl_two = pl_two_name[0].upper()
    print('-----------------------------------------------------------')
    print(pl_one_name+', твой символ -', pl_one)
    print(pl_two_name+ ', твой символ -', pl_two)
    print('-----------------------------------------------------------')
    time.sleep(1)

def show_cells():
    # вывод поля
    print("  0 1 2")
    for i in range(3):
        print(f"{i} {cells[i][0]} {cells[i][1]} {cells[i][2]}")

def rules():
    # вывод правил игры
    print('Игровое поле выглядит так:')
    show_cells()
    print('-----------------------------------------------------------')
    print('                     Правила игры:')
    print('1) Игроки ходят по очереди. За 1 ход ставится 1 знак в поле')
    print('2) Игрок побеждает, если поставит на поле 3 символа в ряд ')
    print('          по вертикали, по горизонтали, либо по диагонали')
    print('3) Ничья - если поле кончилось, а победителя нет')
    print('-----------------------------------------------------------')
    print('                     Порядок ввода:')
    print('Каждая клетка поля имеет свои координаты')
    print('Необходимо ввести через пробел номер строки и номер столбца')
    print('Например:  1 2')
    print('-----------------------------------------------------------')
    time.sleep(1)

def step_check():
    # ход игрока
    while True:
        step = input().split()
        if len(step) != 2:
            print('Введено неверное количество чисел. Введите 2 числа!')
            continue

        i, j = step

        if not (i.isdigit()) or not (j.isdigit()):
            print('Введены неверные символы. Введите 2 числа!')
            continue

        i, j = int(i), int(j)

        if 0 > i or i > 2 or 0 > j or j > 2:
            print('Некорректный ввод. Необходимо ввести 2 числа из диапазона 0-2')
            continue

        if cells[i][j] != " ":
            print('Клетка уже занята, выберите другую!')
            continue
        return i, j

def win_check():
    win = (((0, 0), (0, 1), (0, 2)),  # горизонталь по строке 0
           ((1, 0), (1, 1), (1, 2)),  # горизонталь по строке 1
           ((2, 0), (2, 1), (2, 2)),  # горизонталь по строке 2
           ((0, 0), (1, 0), (2, 0)),  # вертикаль по столбцу 0
           ((0, 1), (1, 1), (2, 1)),  # вертикаль по столбцу 1
           ((0, 2), (1, 2), (2, 2)),  # вертикаль по столбцу 2
           ((0, 0), (1, 1), (2, 2)),  # диагональ 00-22
           ((2, 0), (1, 1), (0, 2)))  # диагональ 20-02

    for step in win:
        symbols = []
        for c in step:
            symbols.append(cells[c[0]][c[1]])
        if symbols == [pl_one, pl_one, pl_one]:
            print('Выиграл', pl_one_name + '!')
            return True

        if symbols == [pl_two, pl_two, pl_two]:
            print('Выиграл', pl_two_name + '!')
            return True
    return False

cells = [[' '] * 3 for i in range(3)]

greeting()
rules()
invite()

steps_count = 0

while steps_count <= 9:
    steps_count += 1
    show_cells()
    if steps_count % 2 == 1:
        print(pl_one_name, ', твой ход: ')
    else:
        print(pl_two_name, ', твой ход: ')

    x, y = step_check()

    if steps_count % 2 == 1:
        cells[x][y] = pl_one
    else:
        cells[x][y] = pl_two

    if win_check():
        show_cells()
        break

    if steps_count == 9:
        show_cells()
        print("Ничья!")
        break