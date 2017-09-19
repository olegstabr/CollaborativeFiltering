# -*- coding: utf-8 -*-
import main


# Расчет среднеквадратической ошибки
def calculate_error(real_rating, calc_rating):
    return pow(real_rating - calc_rating, 2) ** .5


# Тестирование разработанной системы на тестовой выборке
def test_data(path='./data/ml-100k/u1.test'):
    # загружаем тестовые данные
    # вычисляем неизвестные оценки
    # вычисляем ошибку RMSE
    pass
