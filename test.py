# -*- coding: utf-8 -*-
import main


# Расчет среднеквадратической ошибки
def calculate_error(real_rating, calc_rating):
    sum = 0
    n = len(real_rating)
    for i in range(n):
        sum += pow(real_rating[i] - calc_rating[i], 2)
    return (sum / n) ** .5


# Тестирование разработанной системы на тестовой выборке
def test_data(path='./data/ml-100k/u1.test'):
    # загружаем тестовые данные
    # вычисляем неизвестные оценки
    # вычисляем ошибку RMSE
    test_data = {}
    base_data = main.load_data()
    user_id = str(1)
    real_ratings = []
    calc_ratings = []
    with open(path) as file:
        for line in file:
            (user, movieId, rating, timestamp) = line.split("\t")
            test_data.setdefault(user, {})
            test_data[user][movieId] = float(rating)
    ratings = test_data[user_id]
    for movie_id in ratings:
        calc_rating = main.get_rating(base_data, user_id, int(movie_id))
        if calc_rating == 0:
            continue
        calc_ratings.append(calc_rating)
        real_rating = test_data[user_id][movie_id]
        real_ratings.append(real_rating)
    print("Реальные оценки:      %s" % real_ratings)
    print("Предсказанные оценки: %s" % calc_ratings)
    print("Ошибка: %s" % calculate_error(real_ratings, calc_ratings))
        # print('Фильм = %s\nРеальная оценка = %f\nПосчитанная оценка = %f\nОшибка = %f\n' % (
        #     movie_id, real_rating, calc_rating, calculate_error(real_rating, calc_rating)))


def test():
    test_data()


test()
