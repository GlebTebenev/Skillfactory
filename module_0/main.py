import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Функция принимает загаданное число и возвращает число попыток """
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Устанавливаем границы поиска как 0 и 101.
       Берем среднее арифметическое от границ. Если число меньше загаданного, то нижняя граница обновляется.
       Если больше, то обновляется верхняя граница
       Функция принимает загаданное число и возвращает число попыток"""
    lower_bound = 0  # нижняя граница
    upper_bound = 101  # верхняя граница
    predict = (upper_bound + lower_bound) // 2  # среднее число
    count = 1  # попытка 1

    while number != predict:
        count += 1
        if predict < number:
            lower_bound = predict
            predict = (lower_bound + upper_bound) // 2
        elif predict > number:
            upper_bound = predict
            predict = (lower_bound + upper_bound) // 2
        else:
            return count

    if predict == number:
        return count


print(score_game(game_core_v1))
print(score_game(game_core_v2))
print(score_game(game_core_v3))
