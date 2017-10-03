# -*- coding: utf-8 -*-
import user_based
import item_based


# Расчет среднеквадратической ошибки
def calculate_error(real_rating, calc_rating):
    sum = 0
    n = len(real_rating)
    for i in range(n):
        sum += pow(real_rating[i] - calc_rating[i], 2)
    return (sum / n) ** .5


# Тестирование разработанной системы на тестовой выборке
def test_data(path='./data/ml-100k/u1.test', load_data=user_based.load_data):
    # загружаем тестовые данные
    # вычисляем неизвестные оценки
    # вычисляем ошибку RMSE
    test_data = {}
    base_data = load_data()
    user_id = str(1) # Будет искаться оценка для юзера 1 или для фильма 1
    real_ratings = []
    calc_ratings = []
    with open(path) as file:
        for line in file:
            (user, movieId, rating, timestamp) = line.split("\t")
            test_data.setdefault(user, {})
            test_data[user][movieId] = float(rating)
    ratings = test_data[user_id]
    for movie_id in ratings:
        calc_rating = user_based.get_rating(base_data, user_id, int(movie_id), similarity=user_based.sim_distance_2)
        if calc_rating == 0:
            continue
        calc_ratings.append(round(calc_rating, 1))
        real_rating = test_data[user_id][movie_id]
        real_ratings.append(real_rating)
    if load_data == user_based.load_data:
        filter_type = "user_based:"
    else:
        filter_type = "item_based:"
    print filter_type
    print("Реальные оценки:      %s" % real_ratings)
    print("Предсказанные оценки: %s" % calc_ratings)
    print("Ошибка: %s" % calculate_error(real_ratings, calc_ratings))
    print
        # print('Фильм = %s\nРеальная оценка = %f\nПосчитанная оценка = %f\nОшибка = %f\n' % (
        #     movie_id, real_rating, calc_rating, calculate_error(real_rating, calc_rating)))


def test():
    user_based.visualize_R(user_based.load_data())
    test_data()
    test_data(load_data=item_based.load_data)


test()
