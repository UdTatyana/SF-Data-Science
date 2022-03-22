"""Игра угадай число.
Компьютер сам загадывает и угадывает число 
за минимальное количество попыток (меньше 20)
"""

import numpy as np

def min_random_predict(number:int=1) -> int:
    """За какое минимальное количество попыток компьютер угадывает число

    Args:
        number(int, optional): Загаданное число.

    Returns: минимальное количество попыток
    """
    
    min_predict = 1
    max_predict = 101
    number = np.random.randint(min_predict, max_predict) # предполагаемое число
    count = 0
    
    while True:
        count += 1
        predict = round((min_predict + max_predict)/2)

        if number < predict:
            max_predict = predict
        elif number > predict:
            min_predict = predict
        else:    
            return count 
            break  
        
print(f'Число угадано за {min_random_predict()} попыток') 