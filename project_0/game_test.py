"""Игра угадай число.
Компьютер сам загадывает и угадывает число 
за минимальное количество попыток (меньше 20)
"""

import numpy as np

min_predict = 1
max_predict = 101
count = 0

predict_number = np.random.randint(min_predict, max_predict) # предполагаемое число

while True:
    count += 1
    predict = round((min_predict + max_predict)/2)

    if predict_number < predict:
        max_predict = predict
    elif predict_number > predict:
        min_predict = predict
    else:    
        print('Число', predict_number, 'угадано за', count, 'попыток') 
        break   