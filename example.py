# -*- coding: utf-8 -*-
from math import sqrt


# Загрузка данных (пример для movielen)
def load_data(path='./data/ml-100k/u.data'):
    prefs = {}
    for line in open(path):
        (user, movieid, rating, ts) = line.split("\t")
        prefs.setdefault(user, {})
        prefs[user][movieid] = float(rating)
    return prefs


# Визуализация матрицы R
def visualize_R(prefs):
    # реализуйте визуализацию с помощью matplotlib
    pass


# пример реализации функции близости (евклидово расстояние)
def sim_distance_1(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    if len(si) == 0: return 0

    # сложить квадраты разностей
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sum_of_squares)


# реализация функции близости 2
def sim_distance_2(prefs, person1, person2):
    # Реализуйте функцию близости 2
    pass


# Возвращает отранжированных k пользователей
def topMatches(prefs, person, k=5, similarity=sim_distance_1):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:k]


# Получить неизвестную оценку объекта для пользователя
def get_rating(prefs, person, object_id, similarity=sim_distance_1):
    # Посчитать меру близости пользователя со всеми остальными (кроме себя самого)
    # С помощью topMatches найти k самых похожих пользователя
    # Вычислить оценку для объекта object_id
    pass


# Расчет среднеквадратической ошибки
def calculate_error():
    pass


# Тестирование разработанной системы на тестовой выборке
def test_data(path='./data/ml-100k/u.data'):
    # загружаем тестовые данные
    # вычисляем неизвестные оценки
    # вычисляем ошибку RMSE
    pass
