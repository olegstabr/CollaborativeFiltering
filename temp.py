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

# Вычисление коэффициента Пирсона
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


# Реализация функции близости 1 (Коэффициент корреляции Пирсона)
def sim_distance_1(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    common = {}
    for item in prefs[str(person1)]:
        if item in prefs[str(person2)]:
            common[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    if len(common) == 0:
        return 0

    return pearson(prefs[str(person1)], prefs[str(person2)], common)


# Реализация функции близости 2 (Коэффициент Жаккара)
def sim_distance_2(prefs, person1, person2):
    # Получить список предметов, оцененных обоими
    common = {}
    dict1 = prefs[str(person1)]
    dict2 = prefs[str(person2)]
    for item in dict1:
        if item in dict2:
            common[item] = 1

    # Если нет ни одной общей оценки, вернуть 0
    n = len(common)
    if n == 0:
        return 0
    return n / float(len(dict1) + len(dict2) - n)


# Возвращает отранжированных k пользователей
def topMatches(prefs, person, k=5, similarity=sim_distance_1):
    scores = [(similarity(prefs, person, int(other)), other)
              for other in prefs if int(other) != person]
    scores.sort()
    scores.reverse()
    return scores[0:k]


# Получить неизвестную оценку объекта для пользователя
def get_rating(prefs, person, object_id, similarity=sim_distance_1):
    # Посчитать меру близости пользователя со всеми остальными (кроме себя самого)
    # С помощью topMatches найти k самых похожих пользователя
    # Вычислить оценку для объекта object_id
    simmilar = topMatches(prefs, person)
    if str(object_id) in prefs[str(person)]:
        object_rating = prefs[str(person)][str(object_id)]
        print object_rating
    else:
        print "Doesn't exist"


def main():
    prefs = load_data()
    print('Пирсон = %s' % sim_distance_1(prefs, 255, 144))
    print('Жаккар = %s' % sim_distance_2(prefs, 255, 144))
    print('Топ-5 Пирсон = %s' % topMatches(prefs, 255))
    print('Топ-5 Жаккар = %s' % topMatches(prefs, 255, similarity=sim_distance_2))
    get_rating(prefs, 255, 1)

main()
