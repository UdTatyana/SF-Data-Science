""" Игра 'Угадай число' - v.2
(за сколько попыток в среднем алгоритм угадывает число)"""

import numpy as np
from game_v1 import random_predict

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов алгоритм угадывает число

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # список чисел рандомных чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)