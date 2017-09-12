# -*- coding: utf-8 -*-
from scipy.stats.stats import pearsonr


# Загрузка данных из файла
def load_data(path='./data/ml-100k/u.data'):
    prefs = {}
    for line in open(path):
        (user, movieId, rating, timestamp) = line.split("\t")
        prefs.setdefault(user, {})
        prefs[user][movieId] = float(rating)
    return prefs


# Реализация функции близости 1 (Коэффициент корреляции Пирсона)
def sim_distance_1(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    common = {}
    for item in prefs.items()[person1][1]:
        if item in prefs.items()[person2][1]:
            common[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    if len(common) == 0:
        return 0

    return pearson(prefs.values()[person1], prefs.values()[person2], common)


def pearson(x, y, common):
    n = len(common)
    # Простые суммы
    sumX = sum([float(x[i]) for i in common])
    sumY = sum([float(y[i]) for i in common])

    # Суммы квадратов
    sumXSq = sum([x[i] ** 2 for i in common])
    sumYSq = sum([y[i] ** 2 for i in common])
    # Сумма проивзедений
    pSum = sum([x[i] * y[i] for i in common])

    # Коэффициент корреляции Пирсона
    num = pSum - sumX * sumY / n
    den = ((sumXSq - pow(sumX, 2) / n) * (sumYSq - pow(sumY, 2) / n)) ** .5

    if den == 0:
        return 0
    k = num / den
    return k


# Реализация функции близости 2 (Коэффициент Жаккара)
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


def main():
    prefs = load_data()
    print sim_distance_1(prefs, 259, 78)


main()
