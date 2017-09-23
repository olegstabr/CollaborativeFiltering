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
    prefs = {}
    with open(path) as file:
        for line in file:
            (user, movieId, rating, timestamp) = line.split("\t")
            prefs.setdefault(user, {})
            prefs[user][movieId] = float(rating)
    user_id = str(1)
    ratings = prefs[user_id]
    for movie_id in ratings:
        base_data = main.load_data()
        real_rating = prefs[user_id][movie_id]
        calc_rating = main.get_rating(base_data, user_id, int(movie_id))
        if calc_rating == 0:
            continue
        print('Фильм = %s\nРеальная оценка = %f\nПосчитанная оценка = %f\nОшибка = %f\n' % (
            movie_id, real_rating, calc_rating, calculate_error(real_rating, calc_rating)))


def test():
    test_data()


test()
